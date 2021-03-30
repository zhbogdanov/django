from django.db import models
import datetime


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class WorkOrService(models.Model):
    document = models.CharField('Документы', max_length=100)

    def __str__(self):
        return self.document

    class Meta:
        verbose_name = 'Услуга или работа'
        verbose_name_plural = 'Услуги или работы'


class Conditions(models.Model):
    condition = models.CharField('Условия', max_length=100)

    def __str__(self):
        return self.condition

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'


class Side(models.Model):
    side = models.CharField('Cторона', max_length=100)

    def __str__(self):
        return self.side

    class Meta:
        verbose_name = 'Сторона'
        verbose_name_plural = 'Стороны'


class Quality(models.Model):
    quality = models.CharField('Качество', max_length=100)

    def __str__(self):
        return self.quality

    class Meta:
        verbose_name = 'Качество'
        verbose_name_plural = 'Качество'


class Documents(models.Model):
    name_of_the_organization = models.CharField('Название организации',
                                                max_length=100)
    address = models.CharField('Адрес', max_length=100)

    email = models.EmailField('Email', max_length=100)
    subject_of_a_contract = models.ForeignKey(WorkOrService,
                                              verbose_name='Предмет договора',
                                              on_delete=models.CASCADE)
    name_of_the_contract = models.CharField('Наименование договора',
                                            max_length=100)
    quantity = models.IntegerField('Количество')
    number_of_contract = models.TextField('Номер договора',
                                          max_length=100)
    date_of_signing = models.DateField()
    period_of_execution = models.DateField()
    price = models.IntegerField('Цена')
    share_of_payment = models.CharField('Доли платежа',
                                        max_length=100)
    term = models.DateField()
    other_conditions = models.ForeignKey(Conditions,
                                         verbose_name='Иные условия',
                                         on_delete=models.CASCADE)

    # загрузить текст

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Contract(models.Model):
    type = 'Поставки'

    # Общая информация
    date_of_signing = models.DateField('Дата подписания')
    side = models.ForeignKey(Side, verbose_name='Сторона',
                             on_delete=models.CASCADE)
    title = models.CharField('Наименование Организации', max_length=200)
    director = models.CharField('Генеральный директор', max_length=100)
    legal_address = models.CharField('Адрес', max_length=254)
    email = models.EmailField('E-mail', blank=True, max_length=200)  # В данный момент не обязательно к заполнению
    number_of_contract = models.CharField('Номер договора', max_length=250)

    # Условия Договора
    # Предмет логовора
    name = models.CharField('Наименование', max_length=120, default='Компьютеры')
    amount = models.PositiveSmallIntegerField('Количество', default=0)  # от 0 до 32767

    # Порядок исполнения
    delivery_date = models.DateField('Срок поставки', default=datetime.date.today)



    # Оплата
    price = models.FloatField('Цена', default=0.0)
    due_date = models.DateField('Срок оплаты', default=datetime.date.today)


    PAYMENT = 'На этапе оплаты'
    SIGNING = 'На этапе подписывания'
    STATUS_CHOICES = [
        (PAYMENT, 'На этапе оплаты'),
        (SIGNING, 'На этапе подписывания')
    ]
    status = models.CharField(
        'Статус',
        max_length=21,
        choices=STATUS_CHOICES,
        default=SIGNING,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Timing(models.Model):
    DONE = 'Выполнено'
    NOT_DONE = 'Не выполнено'
    REACTION_CHOICES = [
        (DONE, 'Выполнено'),
        (NOT_DONE, 'Не выполнено')
    ]
    name = models.CharField('Наименование', max_length=120, default='')
    contract = models.ForeignKey(Contract, null=True, on_delete=models.SET_NULL)
    today = models.DateField(default=datetime.date.today)
    execution_period = models.DateField('Срок исполнения')
    subject = models.IntegerField('Количество обещанного товара')
    payment_period = models.DateField('Срок оплаты')
    amount = models.DecimalField('Сумма', max_digits=15, decimal_places=2, default=0.0)
    penalty = models.DecimalField('Неустойка', max_digits=15, decimal_places=2, default=0.00)
    days = models.IntegerField('Дни разницы', default=0)
    paid = models.DecimalField('Оплачено', max_digits=15, decimal_places=2, default=0.0)
    delivered = models.IntegerField('Доставлено', default=0)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE, default=1)
    reaction = models.CharField(
        'Реакция',
        max_length=12,
        choices=REACTION_CHOICES,
        default=NOT_DONE,
    )



    # claim = ('Претензия')

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Срок'
        verbose_name_plural = 'Сроки'

    # claim = ('Претензия')


class Book(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media')

    def __str__(self):
        return self.title
