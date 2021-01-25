# Generated by Django 2.2 on 2021-01-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0014_auto_20210115_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentity',
            name='account_number',
            field=models.CharField(max_length=16, null=True, verbose_name='شماره حساب'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=20, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], null=True, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='is_guest',
            field=models.BooleanField(default=False, verbose_name='مهمان هستم'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='mobile_phone_number',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=12, null=True, verbose_name='شماره تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='national_code',
            field=models.CharField(max_length=10, null=True, verbose_name='شماره ملی'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='student_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='شماره دانشجویی'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'admin'), (2, 'simple')], default=2, verbose_name='نوع کاربری دانشجو'),
        ),
        migrations.AlterField(
            model_name='userentity',
            name='year_of_entry',
            field=models.IntegerField(null=True, verbose_name='سال ورودی'),
        ),
    ]
