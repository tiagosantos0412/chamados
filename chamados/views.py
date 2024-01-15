from django.shortcuts import render
from.models import Chamados

# Create your views here.
def listar_chamados(request):
    chamados = Chamados.objects.all()
    return render(request, "chamados/listar_chamados.html", {"chamados": chamados})