from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Mesure   # Assurez-vous que le modèle existe

def dernieres_mesures_api(request):
    # Récupère la dernière mesure (ou les 10 dernières)
    derniere = Mesure.objects.order_by('-date').first()
    if derniere:
        data = {
            'temperature': derniere.temperature,
            'humidite': derniere.humidite,
            'date': derniere.date.isoformat()
        }
    else:
        data = {'error': 'Aucune mesure'}
    return JsonResponse(data)