# Generated by Django 2.2.5 on 2020-05-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_address',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
