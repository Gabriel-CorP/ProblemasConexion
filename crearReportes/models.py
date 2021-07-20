from django.db import models

# Create your models here.


class Departamento(models.Model):
    nombre_departamento=models.CharField(max_length=40)
    
class Municipio(models.Model):
    nombre_municipio=models.CharField(max_length=60)
    departamento=models.ForeignKey(Departamento,
    on_delete=models.CASCADE,)

class Usuario(models.Model):
    dui=models.CharField(max_length=10)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    telefono=models.CharField(max_length=9)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['dui']
    
    def __str__(self):
        return ('Usuario con dui '+ self.dui + ' agregado')


class Direccion(models.Model):
    usuario=models.ForeignKey(Usuario,
    on_delete=models.CASCADE,)
    departamento=models.ForeignKey(Departamento,
    on_delete=models.CASCADE,)
    municipio=models.ForeignKey(Municipio,
    on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
        ordering = ['usuario']
    
    def __str__(self):
        return ('La direccion a sido agregada')

class Tipo_Conexion(models.Model):
    nombre_conexion=models.CharField(max_length=25)
    
class Proveedor(models.Model):
    nombre_proveedor=models.CharField(max_length=25)

class Velocidad(models.Model):
    nombre_velocidad=models.CharField(max_length=10)

class Conexion(models.Model):
    tipo_conexion=models.ForeignKey(Tipo_Conexion,
    on_delete=models.CASCADE,)
    velocidad=models.ForeignKey(Velocidad,
    on_delete=models.CASCADE,)
    proveedor=models.ForeignKey(Proveedor,
    on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Conexion'
        verbose_name_plural = 'Conexiones'
        ordering = ['tipo_conexion']
    
    def __str__(self):
        return ('La conexion de tipo '+ self.tipo + ' fue agregada')

class Tipo_Problema(models.Model):
    nombre_problema=models.CharField(max_length=55)

class Problema(models.Model):
    tipo_problema=models.ForeignKey(Tipo_Problema,
    on_delete=models.CASCADE,)
    descripcion=models.CharField(max_length=300)
    usuario=models.ForeignKey(Usuario,
    on_delete=models.CASCADE,)
    conexion=models.ForeignKey(Conexion,
    on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
        ordering = ['conexion']
    
    def __str__(self):
        return ('Problema de '+ self.tipo_problema + 'agregado')


