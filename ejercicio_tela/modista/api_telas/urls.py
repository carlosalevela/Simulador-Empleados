from .views import calculoTelas
from django.urls import path

urlpatterns=[
    path('medidas/',calculoTelas.as_view()),
]