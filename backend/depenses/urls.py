from django.urls import path
from . import views

urlpatterns = [
    path('depenses/', views.liste_depenses, name='liste_depenses'),
    path('depenses/<int:id>/delete/', views.liste_depenses, name='delete'),
    path('depenses/<int:id>/json/', views.get_depense, name='get_depense'),
    path('depenses/<int:id>/edit/', views.liste_depenses, name='edit')
    
]