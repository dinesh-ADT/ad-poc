from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('fitbit_api/', include('fitbit_api.urls')),
    path('admin/', admin.site.urls),
]

