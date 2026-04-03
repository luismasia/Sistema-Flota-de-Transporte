from django.conf import settings

def informacion_empresa(request):
    return {
        'INFO_EMPRESA': getattr(settings, 'DATOS_EMPRESA', {})
    }