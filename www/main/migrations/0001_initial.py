# Generated by Django 4.2.2 on 2023-06-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=512)),
                ('address_line2', models.CharField(max_length=256)),
                ('parish', models.CharField(max_length=256)),
                ('default_status', models.BooleanField(default=None, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=1024)),
                ('business_category', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.CharField(default='Business', max_length=256)),
            ],
        ),
    ]