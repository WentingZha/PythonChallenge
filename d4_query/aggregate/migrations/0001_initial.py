# Generated by Django 5.0.1 on 2024-02-05 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate.publisher')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregate.book')),
            ],
            options={
                'db_table': 'book_order',
            },
        ),
    ]
