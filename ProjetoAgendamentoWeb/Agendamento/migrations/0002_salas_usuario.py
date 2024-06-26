# Generated by Django 5.0.6 on 2024-06-06 16:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agendamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salas', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=50)),
                ('equipamentos', models.CharField(max_length=50)),
                ('agendamento', models.CharField(default='Disponível', max_length=50)),
                ('horario', models.TimeField(blank=True, null=True)),
                ('agendado_por', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('idade', models.IntegerField()),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('quartos', models.CharField(max_length=50)),
            ],
        ),
    ]
