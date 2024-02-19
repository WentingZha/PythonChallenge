# Generated by Django 5.0.1 on 2024-02-03 03:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0002_category_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='Articles', to='channels.category'),
        ),
    ]
