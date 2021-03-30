# Generated by Django 3.1.2 on 2020-10-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_filesadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='media')),
            ],
        ),
    ]
