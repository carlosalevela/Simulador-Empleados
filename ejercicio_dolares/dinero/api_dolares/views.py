from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status,permissions
import json

class dolares(APIView):
    def get (self, request, *args, **kwargs):
        dolares=request.GET.get('dolares')
        conversion=3824*int(dolares)
        return Response(conversion, status=status.HTTP_200_OK)
    




# Create your views here.
