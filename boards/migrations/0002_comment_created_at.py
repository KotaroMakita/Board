# Generated by Django 3.1.5 on 2021-01-28 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]
