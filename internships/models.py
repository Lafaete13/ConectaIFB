from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CompanyProfile, StudentProfile


class Internship(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='internships', verbose_name='Empresa')
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    area = models.CharField(max_length=100, verbose_name='Área') 
    requirements = models.TextField(blank=True, null=True, verbose_name='Requisitos')
    status = models.CharField(max_length=10, choices=[('aberta', 'Aaberta'), ('fechada', 'Fechada')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return f'{self.title} --> {self.status}'


class Application(models.Model):
    internship = models.ForeignKey(
        Internship,
        on_delete=models.CASCADE,
        related_name='applications_internships', 
        verbose_name='Vaga'
    )
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='applications_students',
        verbose_name='Estudante'
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ('pendente', 'Pendente'),
            ('aprovado', 'Aprovado'),
            ('rejeitado', 'Rejeitado')
        ],
        default='pendente'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Candidatura' 
        verbose_name_plural = 'Candidaturas' 
        unique_together = ('internship', 'student')

    def __str__(self):
        return f'{self.student} --> {self.internship.title}'
