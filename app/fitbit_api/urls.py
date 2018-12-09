from django.urls import path
from . import views

app_name= 'fitbit_api'

urlpatterns = [
    path('', views.index, name='index'),
]