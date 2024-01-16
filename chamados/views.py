from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from.models import Chamados

# Create your views here.
'''
def chamados_list(request):
    chamados = Chamados.objects.all()
    return render(request, "chamados/chamados_list.html", {"chamados": chamados})
'''

class ChamadosListView(ListView):
    model = Chamados

class ChamadosCreateView(CreateView):
    model = Chamados
    fields = ['titulo', 'descricao', 'categoria']
    success_url = reverse_lazy('chamados_list')

class ChamadosUpdateView(UpdateView):
    model = Chamados
    fields = ['status']
    success_url = reverse_lazy('chamados_list')