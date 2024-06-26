# Generated by Django 4.2.7 on 2024-06-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_orderitem_price_orderitem_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_option',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_parish',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_phone',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.CharField(default='Pending', max_length=256),
        ),
    ]
