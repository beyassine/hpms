# Generated by Django 3.2.10 on 2022-05-19 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0022_ronde'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ronde',
            name='intervenant',
        ),
        migrations.AddField(
            model_name='ronde',
            name='intervenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ronde_intervenant'),
        ),
    ]
