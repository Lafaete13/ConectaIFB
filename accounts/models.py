from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', verbose_name='Estudante')
    course = models.CharField(max_length=100, verbose_name='Curso')
    semester = models.PositiveIntegerField(verbose_name='Semestre')
    skills = models.TextField(null=True, blank=True, verbose_name='Habilidades')

    def __str__(self):
        return self.user.username
    

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile', verbose_name='Administrador')
    position = models.CharField(max_length=100, verbose_name='Cargo', default='Coordenador')

    def __str__(self):
        return self.user.username


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile', verbose_name='Empresa')
    cnpj = models.CharField(max_length=18, unique=True)
    industry = models.CharField(max_length=100, verbose_name='Seguimento')

    def __str__(self):
        return self.user.username
    