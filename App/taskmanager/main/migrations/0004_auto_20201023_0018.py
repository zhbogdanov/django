# Generated by Django 3.1.2 on 2020-10-23 00:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201021_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=100, verbose_name='Качество')),
            ],
            options={
                'verbose_name': 'Качество',
                'verbose_name_plural': 'Качество',
            },
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(max_length=100, verbose_name='Cторона')),
            ],
            options={
                'verbose_name': 'Сторона',
                'verbose_name_plural': 'Стороны',
            },
        ),
        migrations.RemoveField(
            model_name='contract',
            name='date_of_creation',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='file',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='period_of_execution',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='subject_of_a_contract',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='terms',
        ),
        migrations.AddField(
            model_name='contract',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Срок поставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Срок оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='part_of_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Сколько поставили'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='part_of_price',
            field=models.IntegerField(default=0, verbose_name='Сколько оплатили'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='quality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.quality', verbose_name='Качество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='side',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.side', verbose_name='Сторона'),
            preserve_default=False,
        ),
    ]
