from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions
import json

class cobro (APIView):
    def get (self, request, *args, **kwargs):
        horas_uso= request.GET.get ('horas')
        precio_hora=request.GET.get ('precio')
        valor_total= int(horas_uso)*int(precio_hora)
        return Response (valor_total, status=status.HTTP_200_OK)

