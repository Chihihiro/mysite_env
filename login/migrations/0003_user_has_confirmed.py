# Generated by Django 2.1.2 on 2018-10-31 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_confirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
