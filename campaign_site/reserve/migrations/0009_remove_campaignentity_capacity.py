# Generated by Django 2.2 on 2020-12-05 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0008_remove_campaignentity_year_of_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaignentity',
            name='capacity',
        ),
    ]