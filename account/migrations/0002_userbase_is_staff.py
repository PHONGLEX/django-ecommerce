# Generated by Django 3.1.7 on 2021-04-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
