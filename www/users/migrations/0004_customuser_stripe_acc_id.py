# Generated by Django 4.2.5 on 2023-10-26 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_sms_token_is_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='stripe_acc_id',
            field=models.CharField(blank=True, default=None, max_length=2056, null=True),
        ),
    ]
