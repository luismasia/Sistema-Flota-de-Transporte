from django import forms
from .models import Camion

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['patente', 'modelo', 'año', 'kilometraje', 'estado', 'chofer_asignado']
        
        widgets = {
            'patente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC-123'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'chofer_asignado': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(CamionForm, self).__init__(*args, **kwargs)
        self.fields['chofer_asignado'].empty_label = "Ninguno"    