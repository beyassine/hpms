# Generated by Django 3.2.10 on 2022-05-19 20:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0023_auto_20220519_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='intervenant',
            field=models.ManyToManyField(related_name='Intervenants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tache',
            name='intervenant',
            field=models.ManyToManyField(related_name='Intervenant', to=settings.AUTH_USER_MODEL),
        ),
    ]