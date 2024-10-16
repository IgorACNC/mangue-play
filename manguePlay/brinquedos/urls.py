from django.urls import path
from . import views

urlpatterns = [
  path('adicionar_brinquedo/', views.adicionar_brinquedo, name='adicionar_brinquedo'),
  path('visualizar_brinquedos/', views.visualizar_brinquedos, name='visualizar_brinquedos')
]
