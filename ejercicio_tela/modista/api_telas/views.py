import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions


class calculoTelas (APIView):
    def get (self, request, *args, **kwargs):
        cantidad_metros=request.GET.get ('metros')
        medidas= float(cantidad_metros)/0.0254
        return Response (medidas,status=status.HTTP_200_OK) 
