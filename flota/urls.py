from django.urls import path
from .views import InicioView, CamionListView, CamionDetailView, CamionCreateView, CamionUpdateView, CamionDeleteView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('camiones/', CamionListView.as_view(), name='camion_list'),
    path('camiones/nuevo/', CamionCreateView.as_view(), name='camion_create'),
    path('camiones/<int:pk>/', CamionDetailView.as_view(), name='camion_detail'),
    path('camiones/<int:pk>/editar/', CamionUpdateView.as_view(), name='camion_update'),
    path('camiones/<int:pk>/eliminar/', CamionDeleteView.as_view(), name='camion_delete'),    
]