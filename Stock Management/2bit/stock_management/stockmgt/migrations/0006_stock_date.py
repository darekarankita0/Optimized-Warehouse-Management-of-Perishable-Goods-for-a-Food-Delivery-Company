# Generated by Django 3.0.3 on 2020-07-14 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgt', '0005_stock_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
