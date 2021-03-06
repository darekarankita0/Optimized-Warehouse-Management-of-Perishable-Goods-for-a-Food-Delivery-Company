# Generated by Django 3.0.3 on 2020-07-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('Drinks', 'Drinks')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issue_by',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
