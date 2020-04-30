from django.db import models
from django.contrib.auth.models import User

class Cliente (models.Model):
    CIF = models.CharField(max_length=9)
    empresa = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return f"CIF: {self.CIF}, Empresa: {self.empresa}, Telefono: {self.telefono}"


class Componente(models.Model):
    codigo = models.CharField(max_length=20, default = '')
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)

    def __str__(self):
        return f"Codigo: {self.codigo}, Modelo: {self.modelo}, Marca: {self.marca}"



class Productos(models.Model):
    referencia = models.CharField(max_length=50)
    precio = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40) #DICCIONARIO DE CATEGORIAS(?
    tipo_componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return f"Referencia: {self.referencia}, Precio: {self.precio}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Categoria: {self.categoria}, Tipo de componentes: {self.tipo_componentes}"

#class Pedido(models.Model):
#   codigo = models.CharField(max_length=20)
#   fecha = models.DateField()
#   datos_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
#  productos = models.ManyToManyField(Productos)
#    cantidad = models.IntegerField()
#    precio_total = models.IntegerField()

 #   def __str__(self):
 #       return f"Codigo: {self.codigo}, Fecha: {self.fecha}, Datos de cliente: {self.datos_cliente}, Productos: {self.productos}, Cantidad: {self.cantidad}, Precio total: {self.precio_total}"


class Pedido(models.Model):
    codigo = models.CharField(max_length=20)
    fecha = models.DateField()
    datos_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    productos = models.ManyToManyField(Productos)
    cantidad = models.IntegerField()
    precio_total = models.IntegerField()

    def __str__(self):
        return f"Codigo: {self.codigo}, Fecha: {self.fecha}, Datos de cliente: {self.datos_cliente}, Productos: {self.productos}, Cantidad: {self.cantidad}, Precio total: {self.precio_total}"


class Usuario(User):
    username = models.CASCADE
    password = models.CASCADE
