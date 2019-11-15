from django.db import models
import datetime

class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    correo = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Restaurante(models.Model):
    CIUDAD = (
        ('BOG', 'Bogota D.C'),
        ('BGA', 'Bucaramanga'),
        ('MDE', 'Medellín'),
        ('CLO', 'Cali'),
    )
    nombre = models.CharField(max_length=80)
    ciudad = models.CharField(max_length=3, choices=CIUDAD)
    direccion = models.CharField(max_length=120)
    #productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    MENU = (
        ('C', 'Comida'),
        ('B', 'Bebida'),
        ('P', 'Postre'),
    )
    nombre = models.CharField(max_length=80)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=MENU)
    precio = models.DecimalField(max_digits=6, decimal_places=3)
    imagen = models.ImageField(upload_to = 'reportes/static/reportes/img', default = 'https://d1ralsognjng37.cloudfront.net/0a51c720-0283-4c22-87d9-6cd7a484d373.jpeg')

    def __str__(self):
        return self.nombre

#class ProductoPedido(models.Model):
#    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#    cantidad = models.IntegerField()
# 
#    def precio_total(self):
#       return self.cantidad * self.producto.precio
#
#    def __str__(self):
#        return str(self.producto) + " (x" + str(self.cantidad) + ")"

class Pedido(models.Model):
    ESTADO = (
        ('ER', 'En repartición'),
        ('EN', 'Entregado'),
        ('CA', 'Cancelado'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto) 
    direccion_envio = models.CharField(max_length=120)
    fecha = models.DateField(auto_now_add=True) 
    estado = models.CharField(max_length=2, choices=ESTADO, default='EN')
    #repartidor = models.OneToOneField(Repartidor, on_delete=models.CASCADE)

#    def pedido_total(self):
#        total = 0
#        for producto_pedido in self.productos.all():
#            total += producto_pedido.precio_total()
#        return total
#    
#    total = property(pedido_total)

    # Función que calcula mediante el id de cada producto el valor total del pedido
    def _total(self):
        total = 0
        for prod_id in Pedido.objects.filter(id=self.id).values('producto'): 
            producto = Producto.objects.get(id=prod_id['producto'])
            total += producto.precio
        return total

    total = property(_total)

    def __str__(self):
        return str(self.id)

class Repartidor(Usuario):
    VEHICULO = (
        ('B', 'Bicicleta'),
        ('M', 'Moto'),
        ('C', 'Carro')
    )

    vehiculo = models.CharField(max_length=1, choices=VEHICULO)
    pedido_asignado = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Reclamo(models.Model):
    TIPO = (
        ('I', 'Pedido incorrecto'),
        ('D', 'Pedido demorado'),
        ('N', 'Pedido no llegó')
    )

    fecha = models.DateField(auto_now_add=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
