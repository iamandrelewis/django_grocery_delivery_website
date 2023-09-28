# Generated by Django 4.2.5 on 2023-09-24 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_amountpaid_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 9, 24, 18, 17, 56, 112887)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='fulfilment_status',
            field=models.CharField(default='Unfulfilled', max_length=512),
        ),
    ]