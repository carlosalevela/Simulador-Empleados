from django.urls import path
from .views import edad_empleados

urlpatterns=[
    path('edad/',edad_empleados.as_view()),
]