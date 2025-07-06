from django.db import models

from accounts.models import AdminProfile, StudentProfile
from django.db import models


class Event(models.Model):
    admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE, related_name='event_admin')
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    location = models.CharField(max_length=100, verbose_name='Local')
    date = models.DateTimeField(verbose_name='Data e Hora do Evento')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.title
    

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventregistration_event', verbose_name='Evento')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='eventregistration_student', verbose_name='Estudante')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = ('event', 'student')

    def __str__(self):
        return f'{self.event.title} --> {self.student.user}'