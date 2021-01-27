# Generated by Django 2.2 on 2021-01-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0015_auto_20210115_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='creation_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='deletion_time',
            field=models.DateField(blank=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='last_update_time',
            field=models.DateField(auto_now=True),
        ),
    ]
