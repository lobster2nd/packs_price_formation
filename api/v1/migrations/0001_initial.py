# Generated by Django 4.2.6 on 2023-10-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasePlanningAnalysisData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('our_warehouse', models.CharField(max_length=200)),
                ('wb_warehouse', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('product', models.PositiveIntegerField()),
                ('cabinet', models.PositiveIntegerField()),
            ],
        ),
    ]
