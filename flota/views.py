from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Camion, Chofer, Viaje
from .forms import CamionForm

class InicioView(TemplateView):
    template_name = 'inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_camiones'] = Camion.objects.count()
        context['total_choferes'] = Chofer.objects.count()
        context['viajes_activos'] = Viaje.objects.filter(estado='en_curso').count()
        return context

class CamionListView(ListView):
    model = Camion
    template_name = 'camiones/camion_list.html'
    context_object_name = 'camiones'

class CamionDetailView(DetailView):
    model = Camion
    template_name = 'camiones/camion_detail.html'
    context_object_name = 'camion'

class CamionCreateView(CreateView):
    model = Camion
    form_class = CamionForm
    template_name = 'camiones/camion_form.html'
    success_url = reverse_lazy('camion_list')

class CamionUpdateView(UpdateView):
    model = Camion
    form_class = CamionForm
    template_name = 'camiones/camion_form.html'
    success_url = reverse_lazy('camion_list')

class CamionDeleteView(DeleteView):
    model = Camion
    template_name = 'camiones/camion_confirm_delete.html'
    success_url = reverse_lazy('camion_list')