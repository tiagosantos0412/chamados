from django.shortcuts import render
from.models import Chamados

# Create your views here.
def chamados_list(request):
    chamados = Chamados.objects.all()
    return render(request, "chamados/chamados_list.html", {"chamados": chamados})