# Generated by Django 2.2 on 2020-12-05 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0007_auto_20201127_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaignentity',
            name='year_of_entry',
        ),
    ]
