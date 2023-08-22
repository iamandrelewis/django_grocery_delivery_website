# Generated by Django 4.2.2 on 2023-08-21 03:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productunit_unit_abbr'),
        ('orders', '0006_orderitem_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderReplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=512)),
                ('fulfilment_status', models.BooleanField(default=False)),
                ('ProductGrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productgrade')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderitem')),
            ],
        ),
    ]