# Generated by Django 3.2.9 on 2021-12-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedagogica', '0001_initial'),
        ('academica', '0002_auto_20211217_1123'),
        ('usuarios', '0002_auto_20211217_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, related_name='DocentesA', to='pedagogica.Asignatura'),
        ),
        migrations.AddField(
            model_name='user',
            name='grupos',
            field=models.ManyToManyField(blank=True, related_name='DocentesG', to='academica.Grupo'),
        ),
    ]
