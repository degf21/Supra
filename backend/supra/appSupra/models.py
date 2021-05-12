from django.db import models


class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Areas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Sub_Areas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    area = models.ForeignKey(
        Areas, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def NombreArea(self):
        return self.area.nombre


class Integrantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    numeroDocumento = models.BigIntegerField()
    subarea = models.ForeignKey(Sub_Areas, null=True, blank=True, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, null=True, blank=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Areas, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def NombreArea(self):
        return self.area.nombre
    
    def NombreDocumento(self):
        return self.documento.nombre

    def NombreSub_Area(self):
        return self.subarea.nombre

'''class Empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    numeroDocumento = models.BigIntegerField()
    subarea = models.ForeignKey(
        Sub_Areas, null=True, blank=True, on_delete=models.CASCADE)
    documento = models.ForeignKey(
        Documento, null=True, blank=True, on_delete=models.CASCADE)
    area = models.ForeignKey(
        Areas, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def NombreArea(self):
        return self.area.nombre'''

    
