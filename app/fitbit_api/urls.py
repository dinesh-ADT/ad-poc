from django.urls import path
from . import views

app_name= 'fitbit_api'

urlpatterns = [
    path('/', views.index, name='index'),
    path('user/<slug:user>/profile_data/', views.profile_data, name='fitbit_profile_data')
]