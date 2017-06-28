# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.CharField(blank=True, max_length=150, verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='article',
            name='domain',
            field=models.CharField(choices=[('INFO', 'Сведения'), ('EDUC', 'Образование'), ('GRAD', 'Выпускникам'), ('STNT', 'Образовательные стандарты')], max_length=100, verbose_name='Область распространения'),
        ),
    ]
