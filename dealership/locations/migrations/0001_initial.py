# Generated by Django 5.0.7 on 2024-07-21 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.country')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('province_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.province')),
            ],
            options={
                'verbose_name': 'Locality',
                'verbose_name_plural': 'Localities',
            },
        ),
    ]
