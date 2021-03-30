from .models import Task, Documents, Contract, Timing, Book
from django.forms import ModelForm, TextInput, Textarea, DateInput, EmailInput, Select, NumberInput, FileInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter',
                'width': '160px',
                'id': 'your name'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
        }


class DocumentsForm(ModelForm):
    class Meta:
        model = Documents
        fields = [
            'name_of_the_organization', 'address',
            'email', 'subject_of_a_contract',
            'name_of_the_contract', 'quantity',
            'number_of_contract', 'date_of_signing',
            'period_of_execution', 'price',
            'share_of_payment', 'term',
            'other_conditions'
            ]
        widgets = {
            'name_of_the_organization': TextInput(attrs={
                'class': 'form-control'
            }),
            'address': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'inputEmail3'
            }),
            'subject_of_a_contract': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
            'name_of_the_contract': TextInput(attrs={
                'class': 'form-control'
            }),
            'quantity': NumberInput(attrs={
                'class': 'form-control'
            }),
            'number_of_contract': TextInput(attrs={
                'class': 'form-control'
            }),
            'date_of_signing': DateInput(attrs={
                'type': 'date',
                'name': 'calendar'
            }),
            'period_of_execution': DateInput(attrs={
                'type': 'date',
                'name': 'calendar'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control'
            }),
            'share_of_payment': TextInput(attrs={
                'class': 'form-control'
            }),
            'term': DateInput(attrs={
                'type': 'date',
                'name': 'calendar'
            }),
            'other_conditions': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
        }


class DeliveryDocumentsForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['date_of_signing', 'delivery_date', 'side', 'title', 'director', 'legal_address',
                  'email', 'number_of_contract']
        widgets = {
            'date_of_signing': DateInput(attrs={
            }),
	    'delivery_date': DateInput(attrs={
            }),
            'side': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'director': TextInput(attrs={
                'class': 'form-control'
            }),
            'legal_address': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'inputEmail3'
            }),
            'number_of_contract': TextInput(attrs={
                'class': 'form-control'
            }),

        }


class TimingForm(ModelForm):
    class Meta:
        model = Timing
        fields = ['contract', 'execution_period', 'subject', 'payment_period',
                  'amount', 'penalty', 'reaction',  'quality', 'name', 'paid', 'delivered']
        widgets = {
            'contract': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
            'execution_period': DateInput(attrs={
            }),
            'subject': NumberInput(attrs={
                'class': 'form-control'
            }),
            'payment_period': DateInput(attrs={
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control'
            }),
            'penalty': NumberInput(attrs={
                'class': 'form-control'
            }),
            'reaction': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
            'quality': Select(attrs={
                'class': 'form-control',
                'id': 'exampleFormControlSelect1'
            }),
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
            'paid': NumberInput(attrs={
                'class': 'form-control'
            }),
            'delivered': NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'file')
