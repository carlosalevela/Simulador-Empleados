from django.urls import path
from .views import salario

urlpatterns = [
    path('nomina', salario.as_view()),
]
