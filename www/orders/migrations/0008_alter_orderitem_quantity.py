# Generated by Django 4.2.2 on 2023-08-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_datestamp_orderreplacement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.CharField(default='1', max_length=512),
        ),
    ]
