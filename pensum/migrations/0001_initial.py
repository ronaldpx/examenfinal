# Generated by Django 2.1.3 on 2018-11-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('seccion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('creidto', models.IntegerField()),
                ('profesor', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='pensum.Asignacion', to='pensum.Materia'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.Grado'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.Materia'),
        ),
    ]
