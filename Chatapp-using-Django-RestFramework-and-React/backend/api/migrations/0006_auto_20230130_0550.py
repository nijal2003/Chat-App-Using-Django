# Generated by Django 3.2.7 on 2023-01-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='booking_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='booking_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
