# Generated by Django 3.2.10 on 2022-09-15 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_alter_ronde_intervenant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteequipement',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='siteequipement',
            name='libelle',
        ),
    ]
