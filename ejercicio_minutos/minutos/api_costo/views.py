from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,permissions

class minuteria (APIView):
    def get (self, request, *args, **kwargs):
        valor_minuto=request.GET.get ('precio')
        tiempo= request.GET.get ('minutos')
        valor_total=int(valor_minuto)*int(tiempo)
        return Response (valor_total, status=status.HTTP_200_OK)
    

