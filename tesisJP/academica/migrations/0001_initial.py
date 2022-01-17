# Generated by Django 3.2.9 on 2021-12-17 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedagogica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'tipo persona',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('curp', models.CharField(max_length=50)),
                ('tipoPersona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='academica.tipospersona')),
            ],
            options={
                'verbose_name_plural': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=50)),
                ('asignaturas', models.ManyToManyField(blank=True, related_name='GruposA', to='pedagogica.Asignatura')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedagogica.semestre')),
            ],
            options={
                'verbose_name_plural': 'Grupo',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedulaProfecional', models.CharField(max_length=50)),
                ('asignaturas', models.ManyToManyField(blank=True, related_name='DocentesA', to='pedagogica.Asignatura')),
                ('grupos', models.ManyToManyField(blank=True, related_name='DocentesG', to='academica.Grupo')),
                ('tipoPersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academica.persona')),
            ],
            options={
                'verbose_name_plural': 'Cedula Profecional',
            },
        ),
    ]
