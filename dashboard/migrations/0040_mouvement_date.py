# Generated by Django 3.2.10 on 2022-09-22 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_remove_mouvement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouvement',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
