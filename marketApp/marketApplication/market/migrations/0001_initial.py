# Generated by Django 5.1.7 on 2025-03-19 13:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('telephone_number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('home', models.BooleanField(default=False)),
                ('code', models.IntegerField()),
                ('type', models.CharField(choices=[('food', 'храна'), ('drink', 'пијалок'), ('bakery', 'пекара'), ('cosmetics', 'козметика'), ('hygiene', 'хигиена')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('open_date', models.DateField()),
                ('number_of_market', models.IntegerField()),
                ('working_hours_from', models.TimeField()),
                ('working_hours_to', models.TimeField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contact_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.contactinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('embg', models.CharField(max_length=50)),
                ('paycheck', models.IntegerField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.market')),
            ],
        ),
        migrations.CreateModel(
            name='MarketProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
            ],
        ),
    ]
