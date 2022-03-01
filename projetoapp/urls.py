from django.urls import path, include
from .views import hello_home
from projetoapp import views


urlpatterns = [
    path('', hello_home),
    path('modelform/', views.form_modelform, name="form_modelform")
]