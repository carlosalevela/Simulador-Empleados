from django.urls import path
from .views import dolares

urlpatterns=[
    path('conversion/',dolares.as_view())
]