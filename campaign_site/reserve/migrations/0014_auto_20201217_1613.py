# Generated by Django 2.2 on 2020-12-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0013_auto_20201208_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignentity',
            name='cancel_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaignentity',
            name='is_canceled',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='registeredusers',
            name='cancel_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registeredusers',
            name='is_canceled',
            field=models.BooleanField(default=0),
        ),
    ]
