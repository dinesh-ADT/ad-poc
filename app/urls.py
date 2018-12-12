from django.contrib import admin
from django.urls import path, include
import app.fitbit_api.urls as fitbit_api_urls
from . import views

urlpatterns = [
	path('fitbit_api/', include(fitbit_api_urls, namespace='fitbit_api')),
    path('admin/', admin.site.urls),
]

