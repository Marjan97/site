# Generated by Django 2.2 on 2020-10-12 17:28

import commons.models.base_entity
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('year_of_entry', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_verified', models.BooleanField()),
                ('verification_time', models.DateTimeField(blank=True, null=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='campaigns', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(commons.models.base_entity.BaseEntity, models.Model),
        ),
    ]