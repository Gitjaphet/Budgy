from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('resume/', views.resume, name='resume'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]