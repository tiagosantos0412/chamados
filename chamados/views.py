from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
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

class ChamadosDeleteView(DeleteView):
    model = Chamados
    success_url = reverse_lazy('chamados_list')

class ChamadosCompleteView(View):
    def get(self, request, pk):
        chamados = get_object_or_404(Chamados, pk = pk)
        chamados.encerrado_em = date.today()
        chamados.status = 3
        chamados.save()
        return redirect('chamados_list')

    
