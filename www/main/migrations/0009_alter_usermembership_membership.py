# Generated by Django 4.2.7 on 2024-06-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_usersettings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='membership',
            field=models.CharField(blank=True, default='None', max_length=256, null=True),
        ),
    ]
