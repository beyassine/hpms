# Generated by Django 3.2.10 on 2022-05-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20220519_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.equipement', verbose_name='Equipement')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.site', verbose_name='Site')),
            ],
        ),
    ]
