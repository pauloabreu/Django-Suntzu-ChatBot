# Generated by Django 3.2.12 on 2022-02-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pair_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairmessage',
            name='value',
            field=models.CharField(default='', max_length=500),
        ),
    ]
