from datetime import date
from django.db import models

# Create your models here.
class Chamados(models.Model):
    CATEGORIA_CHOICES = [
        (1, 'Software'),
        (2, 'Hardware')
    ]

    STATUS_CHOICES = [
        (1, 'Novo'),
        (2, 'Em Resolução'),
        (3, 'Resolvido')
    ]

    titulo = models.CharField(max_length= 100, null= False, blank=False) 
    descricao = models.TextField(null=False, blank=False)
    criado_em = models.DateField(auto_now_add=True, null=False, blank=False)
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES, null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, null=False, blank=False)
    encerrado_em = models.DateField(null=True)

    class Meta:
        ordering = ['status']

    def mark_has_complete(self):
        if not self.status == 3:
            self.encerrado_em = date.today()
            self.status = 3
            self.save()         

