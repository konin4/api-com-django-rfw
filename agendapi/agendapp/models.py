from django.db import models

class Login(models.Model):
    # class Meta:
    #     db_table = 'login'
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

class Agenda(models.Model):
    # class Meta:
    #     db_table = 'agenda'
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    login = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='agenda')
    # login = models.ForeignKey(Login, related_name='agenda')
    # login = models.ForeignKey(Login, )
