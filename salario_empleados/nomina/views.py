from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status, permissions

class salario (APIView):
    def get (self,request,*args, **kwargs):
        nombre_empleado= request.GET.get('nombre')
        horas_trabajadas= int (request.GET.get('horastrabajadas'))
        tarifa_hora= int (request.GET.get( 'tarifahora'))
        salario_mes= 2000
        impuesto_mes1= 0.2
        impuestos_mes2= 0.3
        
        
        if horas_trabajadas <= 35:
            salario=  horas_trabajadas * tarifa_hora
        else:
            horas_normales= 35
            extras= horas_trabajadas - horas_normales
            salario= (horas_normales * tarifa_hora) + (extras *1.5* tarifa_hora)
            
        if salario > 2000 and salario <= 2220:
            salario-=salario*impuesto_mes1
        elif salario >2220 :
            salario-=salario*impuestos_mes2
        
        return  Response({"Nombre del empleado":nombre_empleado,"Salario total del mes":salario},status=status.HTTP_200_OK)
            
            
       
        
        
    
        
        
            
            
            
            
        


