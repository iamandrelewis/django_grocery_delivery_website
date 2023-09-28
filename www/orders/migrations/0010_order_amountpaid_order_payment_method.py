# Generated by Django 4.2.2 on 2023-09-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_creditused_order_hascredit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Amountpaid',
            field=models.CharField(default='0', max_length=128),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
