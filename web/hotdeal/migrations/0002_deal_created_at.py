# Generated by Django 3.1.7 on 2021-03-27 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotdeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
