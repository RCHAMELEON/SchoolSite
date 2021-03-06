# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 08:40
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('domain', models.CharField(choices=[('INFO', 'Сведения'), ('EDUC', 'Образование')], max_length=100, verbose_name='Область распространения')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка анонса')),
            ],
        ),
    ]
