from django.contrib import admin
from django.urls import path, include
from .views import hello_teste

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', hello_teste),
    path('', include('projetoapp.urls')),
]
