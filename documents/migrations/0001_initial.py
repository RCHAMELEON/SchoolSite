# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название документа')),
                ('desctiption', models.TextField(blank=True, verbose_name='Описание')),
                ('document_type', models.CharField(choices=[('Education', 'Образование'), ('Testimonies', 'Свидетельства'), ('Treaty', 'Договоры'), ('Regulations', 'Правила'), ('Local Acts', 'Локальные акты'), ('Varification', 'Акты проверки'), ('Schedule', 'Расписания')], max_length=50, verbose_name='Тип документа')),
                ('fiel', models.FileField(blank=True, upload_to='documents/%Y/%m', verbose_name='Файл')),
            ],
        ),
    ]
