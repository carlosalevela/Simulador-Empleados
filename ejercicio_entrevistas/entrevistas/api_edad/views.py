from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class edad_empleados(APIView):
    def get(self, request, *args, **kwargs):
        fecha_nacimiento = request.GET.get('fecha')
        fecha_hoy = request.GET.get('hoy')

        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d-%m-%Y')
        fecha_hoy = datetime.strptime(fecha_hoy, '%d-%m-%Y')
        
        edad = fecha_hoy.year - fecha_nacimiento.year

        return Response(edad, status=status.HTTP_200_OK)
