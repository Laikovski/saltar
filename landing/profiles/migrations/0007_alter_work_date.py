# Generated by Django 3.2.4 on 2021-08-17 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_work_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
