from django.urls import path
from . import views

urlpatterns = [
    path('api/dernieres-mesures/', views.dernieres_mesures_api, name ='api_dernieres_mesures'),]