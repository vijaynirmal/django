# Generated by Django 2.0.1 on 2018-01-12 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 13, 26, 11, 727046, tzinfo=utc), verbose_name='created'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=datetime.datetime(2018, 1, 12, 13, 26, 19, 511980, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]