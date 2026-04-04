from django.http import HttpResponse

def hello_gsi4(request):
 return HttpResponse("Hello GSI4 i'm Fatima Zahra")

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import DHT11

def dashboard(request):
    mesure = DHT11.objects.order_by('-date').first()
    return render (request, 'dashboard.html', {'mesure': mesure})