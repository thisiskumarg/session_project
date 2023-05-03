from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession, name='setsession'),
    path('get/', views.getsession, name='getsession'),
    path('del/', views.delsession, name='delsession'),
]