# Generated by Django 3.2.10 on 2022-03-02 21:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0017_auto_20220227_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='intervenan',
            field=models.ManyToManyField(blank=True, related_name='Intervenan', to=settings.AUTH_USER_MODEL),
        ),
    ]
