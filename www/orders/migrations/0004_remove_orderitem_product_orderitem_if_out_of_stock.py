# Generated by Django 4.2.2 on 2023-08-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_delivery_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='if_out_of_stock',
            field=models.TextField(blank=True, null=True),
        ),
    ]
