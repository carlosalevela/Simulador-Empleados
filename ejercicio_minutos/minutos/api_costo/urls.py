from django.urls import path
from .views import minuteria

urlpatterns=[
    path('valor/',minuteria.as_view()),
]