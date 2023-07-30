# Generated by Django 3.2.20 on 2023-07-30 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='definitions',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
