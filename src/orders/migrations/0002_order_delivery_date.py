# Generated by Django 2.2.5 on 2020-05-14 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]