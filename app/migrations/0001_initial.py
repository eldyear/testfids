# Generated by Django 5.1.2 on 2024-10-27 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Авиакомпания')),
                ('code', models.CharField(blank=True, max_length=3, unique=True, verbose_name='Код авиакомпании')),
                ('logo', models.ImageField(blank=True, upload_to='airline_logos/', verbose_name='Логотип')),
                ('svg_logo', models.FileField(blank=True, upload_to='airline_logos/svg/', verbose_name='SVG логотип')),
            ],
            options={
                'verbose_name': 'Авиакомпания',
                'verbose_name_plural': 'Авиакомпании',
                'db_table': 'Airline',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name_ru', models.CharField(max_length=50, verbose_name='Город на русском')),
                ('city_name_ky', models.CharField(max_length=50, verbose_name='Город на кыргызском')),
                ('city_name_en', models.CharField(max_length=50, verbose_name='Город на английском')),
                ('iata_code', models.CharField(max_length=3, verbose_name='IATA код')),
                ('icao_code', models.CharField(blank=True, max_length=4, verbose_name='ICAO код')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='FlightNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flights', models.CharField(max_length=10, unique=True, verbose_name='№ Рейса ')),
            ],
            options={
                'verbose_name': '№ Рейса',
                'verbose_name_plural': '№ Рейсов',
                'db_table': 'FlightNumber',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_id', models.CharField(blank=True, max_length=2, null=True, unique=True, verbose_name='ID статуса')),
                ('name_ru', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Статус на русском')),
                ('name_ky', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Статус на кыргызском')),
                ('name_en', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Статус на английском')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Stoiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stoiki', models.CharField(max_length=2, unique=True, verbose_name='Стойка № ')),
            ],
            options={
                'verbose_name': '№ Стойки',
                'verbose_name_plural': '№ Стоек',
                'db_table': 'Stoiki',
            },
        ),
        migrations.CreateModel(
            name='InfTablo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('dep', 'Вылет'), ('arr', 'Прилет')], default='', max_length=10, verbose_name='Направление *')),
                ('date1', models.DateField(verbose_name='Дата плановая*')),
                ('time1', models.TimeField(verbose_name='Время плановая*')),
                ('arr_time', models.TimeField(null=True, verbose_name='Время пприбытия*')),
                ('last_date', models.DateField(blank=True, null=True, verbose_name='Дата (факт)')),
                ('last_time', models.TimeField(blank=True, null=True, verbose_name='Время (факт)')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inftablo_airline', to='app.airline', verbose_name='Авиакомпания *')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cities', verbose_name='Пункт назначение *')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.flightnumber', verbose_name='Рейс № *')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.status', verbose_name='Статус')),
                ('stoika', models.ManyToManyField(blank=True, related_name='CheckDesk', to='app.stoiki', verbose_name='Табло №')),
            ],
            options={
                'verbose_name': '"Суточный план"',
                'verbose_name_plural': 'Суточный план',
                'db_table': 'InfTablo',
            },
        ),
    ]
