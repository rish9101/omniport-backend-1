# Generated by Django 2.0.4 on 2018-04-28 23:51

import swapper

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0002_add_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=127)),
                ('designation', models.CharField(blank=True, max_length=127)),
                ('post', models.CharField(blank=True, max_length=127)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=swapper.get_model_name('kernel', 'Person'))),
            ],
            options={
                'swappable': swapper.swappable_setting('kernel', 'Maintainer'),
            },
        ),
    ]