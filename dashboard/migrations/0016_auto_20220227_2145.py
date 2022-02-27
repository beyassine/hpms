# Generated by Django 3.2.10 on 2022-02-27 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_intervention_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='statut',
            field=models.CharField(choices=[('Enregistrée', 'Enregistrée'), ('Pris en charge', 'Pris en charge'), ('Travaux en cours', 'Travaux en cours'), ('Pending', 'Pending'), ('Résolue', 'Résolue')], default='Enregistrée', max_length=100),
        ),
        migrations.AddField(
            model_name='planification',
            name='zone',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.zone', verbose_name='Zone'),
        ),
    ]