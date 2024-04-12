from django.urls import path
from .views import cobro

urlpatterns=[
    path('cobro/',cobro.as_view(),)
]