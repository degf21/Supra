from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status, serializers, viewsets
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from .models import Areas, Documento, Integrantes, Sub_Areas
from .serializers import AreasSerializer, EmpleadoSerializer, Sub_AreasSerializer, DocumentoSerializer

# Create your views here.

class AreasApi(viewsets.ModelViewSet):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer

class DocumentoApi(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class EmpleadosApi(viewsets.ModelViewSet):
    queryset = Integrantes.objects.all()
    serializer_class = EmpleadoSerializer

class Sub_AreasApi(viewsets.ModelViewSet):
    queryset = Sub_Areas.objects.all()
    serializer_class = Sub_AreasSerializer



'''@api_view(['GET'])
def documento_listado(request):
    if request.method == 'GET':
        documento = Documento.objects.all()

        resultados = []

        for doc in documento:
            resultados.append({
                'id': doc.id,
                'nombre': doc.nombre
            })
        print(resultados)


        documento_serializer = json.dumps(resultados)
    
    return HttpResponse(documento_serializer, content_type='application/json')

@api_view(['GET'])
def areas_listado(request):
    if request.method == 'GET':
        areas = Areas.objects.all()

        resultados = []

        for area in areas:
            resultados.append({
                'id': area.id,
                'nombre': area.nombre
            })
        print(resultados)

        areas_serializer = json.dumps(resultados)
    
    return HttpResponse(areas_serializer, content_type='application/json')

@api_view(['GET'])
def empleados_listado(request):
    if request.method == 'GET':
        empleados = Empleados.objects.all()

        resultados = []

        for empleado in empleados:
            resultados.append({
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellido': empleado.apellido,
                'numeroDocumento': empleado.numeroDocumento,
                'id_documento': empleado.documento_id,
                'id_subarea': empleado.subarea_id,
                'id_area': empleado.area_id
            })
        print(resultados)

        empleados_serializer = json.dumps(resultados)
    
    return HttpResponse(empleados_serializer, content_type='application/json')

@api_view(['GET'])
def sub_areas_listado(request):
    if request.method == 'GET':
        sub_areas = Sub_Areas.objects.all()

        resultados = []

        for sub_area in sub_areas:
            resultados.append({
                'id': sub_area.id,
                'nombre': sub_area.nombre,
                'area': sub_area.area_id,
            })
        print(resultados)

        sub_areas_serializer = json.dumps(resultados)
    
    return HttpResponse(sub_areas_serializer, content_type='application/json')'''