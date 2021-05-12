from django.shortcuts import render
from rest_framework import serializers
from .models import Areas, Documento, Sub_Areas, Integrantes

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('id','nombre')

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ('id','nombre')

class Sub_AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Areas
        fields = ('id','nombre','area', 'NombreArea')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrantes
        fields = ('id','nombre','apellido', 'numeroDocumento', 'subarea', 'documento', 'area', 'NombreArea', 'NombreDocumento', 'NombreSub_Area')

'''class DocumentoSerializer(serializers.ModelSerializer):
    documento = serializers.SerializerMethodField()

    def get_documento(self, object: Documento):
        output = []

        for documento in object.documento_set.all():
            output.append({
                'id': documento.id,
                'nombre': documento.nombre
            })
        print(output)
        return output

    class Meta:
        model = Documento
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()

    def get_areas(self, object: Areas):
        output = []

        for area in object.area_set.all():
            output.append({
                'id': area.id,
                'nombre': area.nombre
            })
        print(output)
        return output

    class Meta:
        model = Areas
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    empleado = serializers.SerializerMethodField()

    def get_empleados(self, object: Empleados):
        output = []

        for empleado in object.area_set.all():
            output.append({
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellido': empleado.apellido,
                'numeroDocumento': empleado.numeroDocumento,
                'id_documento': empleado.documento_id,
                'id_subarea': empleado.subarea_id,
                'id_area': empleado.area_id
            })
        print(output)
        return output

    class Meta:
        model = Empleados
        fields = '__all__'

class Sub_AreasSerializer(serializers.ModelSerializer):
    sub_area = serializers.SerializerMethodField()

    areas = serializers.SerializerMethodField()

    def get_sub_areas(self, object: Sub_Areas):
        output = []

        for sub_area in object.sub_area_set.all():
            output.append({
                'id': sub_area.id,
                'nombre': sub_area.nombre,
                'area': object.area_set.all(sub_area.area_id).nombre                
            })
        print(output)
        return output

    class Meta:
        model = Sub_Areas
        fields = '__all__'
        '''
