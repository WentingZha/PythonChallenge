# Generated by Django 5.0.1 on 2024-02-07 01:07

import aggregate.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregate', '0002_alter_bookorder_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=aggregate.models.pubilsher_default, on_delete=django.db.models.deletion.SET_DEFAULT, to='aggregate.publisher'),
        ),
    ]