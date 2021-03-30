from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Documents, Contract, Timing, Side, Quality, Book
from .forms import ContractForm, TimingForm, DocumentsForm, DeliveryDocumentsForm, BookForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.files.storage import FileSystemStorage
from docxtpl import DocxTemplate
import datetime
import decimal

user_email = 'hhh'
cal_form = {'date': '',
            'title': ''}


def parse_date(date):
    return date[6:] + date[3:5] + date[0:2]


def parse_date3(date):
    date = date.split('.')
    return date[2] + '-' + date[1] + '-' + date[0]


def parse_date2(date):
    date = str(date)
    return date[8:10] + '.' + date[5:7] + '.' + date[:4]


def index(request):
    user_email = 'q@m.com'
    contracts = Contract.objects.all()# filter(email=user_email)
    documents = Documents.objects.filter(email=user_email)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'documents': documents,
                                               'user': user_email, 'contracts': contracts})


def create_contract(request):
    form = DeliveryDocumentsForm()
    if request.method == 'POST':
        form = DeliveryDocumentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/create_delivery_contract.html', context)


def update_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    form = DeliveryDocumentsForm(instance=contract)

    if request.method == 'POST':
        form = DeliveryDocumentsForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'contract': contract}
    return render(request, 'main/create_delivery_contract.html', context)


def delete_contract(request, pk):
    contract = Contract.objects.get(id=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('/')

    context = {'item': contract}
    return render(request, 'main/delete_contract.html', context)


def create_timing(request, kek):
    contract = Contract.objects.get(id=kek)
    side1 = Side.objects.get(side='Поставщик')
    side2 = Side.objects.get(side='Покупатель')
    form = TimingForm(initial={'contract': contract})
    if request.method == 'POST':
        form = TimingForm(request.POST)
        if form.is_valid():
            form.save()
            title = ''
            start_data = ''
            end_data = ''
            title = 'Необходимо оплатить ' + contract.name + ' в размере ' + form['amount'].value() + 'руб'
            start_data1 = parse_date(form['payment_period'].value()) + 'T100000Z'
            end_data1 = parse_date(form['payment_period'].value()) + 'T200000Z'
            res1 = ''
            title = title.split()
            for elem in title:
                res1 += elem + '%20'
            res1 = res1[:-3]

            title = 'Необходимо поставить ' + contract.name + ' в размере ' + form['subject'].value() + 'ед'
            start_data2 = parse_date(form['execution_period'].value()) + 'T100000Z'
            end_data2 = parse_date(form['execution_period'].value()) + 'T200000Z'
            res2 = ''
            title = title.split()
            for elem in title:
                res2 += elem + '%20'
            res2 = res2[:-3]
            if contract.side == side2:
                send_link = 'http://www.google.com/calendar/event?action=TEMPLATE&text=' + res1 + '&dates=' + start_data1 + '/' + end_data1
                send_mail('Add to calendar', send_link, 'zhbogdanov@mail.ru', [contract.email], fail_silently=False)

                send_link = 'http://www.google.com/calendar/event?action=TEMPLATE&text=' + res2 + '&dates=' + start_data2 + '/' + end_data2
                send_mail('Add to calendar', send_link, 'zhbogdanov@mail.ru', ['cpinternship2020@gmail.com'], fail_silently=False)
            else:
                send_link = 'http://www.google.com/calendar/event?action=TEMPLATE&text=' + res2 + '&dates=' + start_data2 + '/' + end_data2
                send_mail('Add to calendar', send_link, 'zhbogdanov@mail.ru', [contract.email], fail_silently=False)

                send_link = 'http://www.google.com/calendar/event?action=TEMPLATE&text=' + res1 + '&dates=' + start_data1 + '/' + end_data1
                send_mail('Add to calendar', send_link, 'zhbogdanov@mail.ru', ['cpinternship2020@gmail.com'], fail_silently=False)
            return redirect('/')
    context = {'form': form,
               'contract': contract}
    return render(request, 'main/create_timing.html', context)


def update_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    form = TimingForm(instance=timing)

    if request.method == 'POST':
        form = TimingForm(request.POST, instance=timing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'main/create_timing.html', context)


def delete_timing(request, kek):
    timing = Timing.objects.get(id=kek)
    if request.method == "POST":
        timing.delete()
        return redirect('/')

    context = {'item': timing}
    return render(request, 'main/delete_timing.html', context)


def table(request, contract_id):
    days = 0
    contract = Contract.objects.get(id=contract_id)
    timing = contract.timing_set.all()
    side_pos = Side.objects.get(side='Поставщик')
    side_pok = Side.objects.get(side='Покупатель')
    quality_bad = Quality.objects.get(quality='Неудовлетворительное')
    quality_good = Quality.objects.get(quality='Удовлетворительное')
   
    # Получение и обновление даты today
    n = datetime.datetime.date(datetime.datetime.now())
  
    # Начисление неустойки
    for i in timing:
        if i.contract.side == side_pok and i.reaction == 'Не выполнено' and n > i.execution_period:
            days = (n - i.execution_period).days
            if days > i.days:
                i.penalty += round(decimal.Decimal(0.1 * abs(-i.days + days)) *
                                   (i.subject - i.delivered) * i.amount / i.subject, 2)
                i.days = days
                i.save()
        elif i.contract.side == side_pos and i.reaction == 'Не выполнено' and n > i.payment_period:
            days = (n - i.payment_period).days
            if days > i.days:
                i.penalty += round(decimal.Decimal(0.1 * abs(-i.days + days))
                                   * (i.amount - i.paid), 2)
                i.days = days
                i.save()

    context = {'title': 'Сроки договора', 'contract': contract, 'timing': timing,
               'side_pos': side_pos, 'side_pok': side_pok, 'quality_bad': quality_bad,
               'quality_good': quality_good, 'n': n, 'days': days}
    return render(request, 'main/table.html', context)


def create_delivery_contract(request):
    error = ''
    if request.method == 'POST':
        form = DeliveryDocumentsForm(request.POST)
        if form.is_valid():
            form.save()
            contract = Contract.objects.last()
            return redirect('create_timing', contract.id)
        else:
            error = 'Форма была неверной'

    form = DeliveryDocumentsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_delivery_contract.html', context)


def penalty_to_us(request):
    return render(request, 'main/claim_to_us.html')


def upload_doc(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'main/upload_doc.html')


def penalty_to_another_side_reaction(request, pk):
    timing = Timing.objects.get(id=pk)
    contract = timing.contract
    dif_date = datetime.date.today() - contract.date_of_signing
    dif_date = str(dif_date).split()[0] + '_________'
    doc = DocxTemplate('media/template_post.docx')
    context = {'title': contract.title, 'director': contract.director, 'legal_address': contract.legal_address,
               'date_of_signing': parse_date2(contract.date_of_signing), 'title2': contract.title,
               'number_of_contract': contract.number_of_contract, 'name': timing.name,
               'amount': timing.subject, 'delivery_date': parse_date2(timing.execution_period),
               'due_date': parse_date2(timing.payment_period), 'dif_date': dif_date, 'penalty': timing.penalty,
               'date_of_signing1': parse_date2(contract.date_of_signing),
               'number_of_contract1': contract.number_of_contract}
    doc.render(context)
    
    doc.save('media/Претензия поставка.docx')
    context.pop('dif_date')
    doc = DocxTemplate('media/template_post2.docx')
    doc.render(context)
    doc.save('media/Претензия поставка отмена.docx')
    return render(request, 'main/penalty_to_another_side_reaction.html')


def penalty_to_another_side_quality(request, pk):
    timing = Timing.objects.get(id=pk)
    contract = timing.contract
    penalty = '8,765'
    doc = DocxTemplate('media/template_post3.docx')
    context = {'title': contract.title, 'director': contract.director, 'legal_address': contract.legal_address,
               'date_of_signing': parse_date2(contract.date_of_signing), 'title2': contract.title,
               'number_of_contract': contract.number_of_contract, 'name': timing.name,
               'amount': timing.subject, 'amount2': timing.subject,
               'date_of_signing1': parse_date2(contract.date_of_signing),
               'number_of_contract1': contract.number_of_contract}
    doc.render(context)
    doc.save('media/Претензия качество.docx')
    return render(request, 'main/Претензия качество.html')


def penalty_to_another_side_pay(request, pk):
    timing = Timing.objects.get(id=pk)
    contract = timing.contract
    dif_date = datetime.datetime.now() + datetime.timedelta(days=15)
    print(dif_date)
    doc = DocxTemplate('media/template_post4.docx')
    context = {'title': contract.title, 'director': contract.director, 'legal_address': contract.legal_address,
               'date_of_signing': parse_date2(contract.date_of_signing), 'title2': contract.title,
               'number_of_contract': contract.number_of_contract, 'name': timing.name,
               'amount': timing.subject, 'dif_date': dif_date, 'amount1': timing.amount,
               'date_of_signing1': parse_date2(contract.date_of_signing),
               'number_of_contract1': contract.number_of_contract}
    doc.render(context)
    doc.save('media/Претензия оплата.docx')
    return render(request, 'main/penalty_to_another_side_pay.html')

