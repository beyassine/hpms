# Generated by Django 3.2.10 on 2022-09-13 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0031_auto_20220913_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ronde',
            name='intervenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Intervenant'),
        ),
    ]
