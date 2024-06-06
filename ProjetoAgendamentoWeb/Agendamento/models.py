from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Importa o modelo de usuário do Django
# Create your models here.
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quartos = models.CharField(max_length=50)

from django.core.exceptions import ValidationError

from django.utils import timezone
from datetime import time


class Salas(models.Model):
    salas = models.CharField(max_length=50)
    descricao = models.TextField(max_length=50)
    equipamentos = models.CharField(max_length=50)
    agendamento = models.CharField(max_length=50, default='Disponível')
    horario = models.TimeField(null=True, blank=True)
    agendado_por = models.CharField(max_length=150, null=True, blank=True)  # Alterado para CharField

    def clean(self):
        super().clean() 
        if self.horario:
            if not (timezone.datetime.strptime("07:05", "%H:%M").time() <= self.horario <= timezone.datetime.strptime("17:10", "%H:%M").time()):
                raise ValidationError("O horário de agendamento deve ser entre 7:05 e 17:10.")

    @classmethod
    def all_hours_booked(cls):
        start_time = time(7, 5)
        end_time = time(17, 10)
        booked_hours = cls.objects.filter(horario__range=(start_time, end_time))
        # Verifica se todos os horários entre 7:05 e 17:10 estão ocupados
        if booked_hours.count() >= (end_time.hour - start_time.hour) * 60 + (end_time.minute - start_time.minute) // 5:
            return True
        return False

    def __str__(self):
        return self.salas