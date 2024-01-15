from django.db import models

# Create your models here.
class Chamados(models.Model):
    CATEGORIA_CHOICES = [
        (1, 'Software'),
        (2, 'Hardware')
    ]

    titulo = models.CharField(max_length= 100, null= False, blank=False) 
    descricao = models.TextField(null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True, null=False, blank=False)
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES, null=False, blank=False)
    encerrado_em = models.DateField(null=True)