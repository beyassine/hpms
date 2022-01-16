# Generated by Django 3.1.6 on 2021-12-22 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='', max_length=1000, verbose_name='Désignation')),
                ('libelle', models.CharField(default='', max_length=100, verbose_name='Libellé')),
                ('clientsite', models.ManyToManyField(blank=True, related_name='clientsite', to=settings.AUTH_USER_MODEL)),
                ('intervenantsite', models.ManyToManyField(blank=True, related_name='intervenantsite', to=settings.AUTH_USER_MODEL)),
                ('responsablesite', models.ManyToManyField(blank=True, related_name='responsablesite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
