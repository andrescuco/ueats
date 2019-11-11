from django.db import models

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
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    restaurante = models.OneToOneField(Restaurante, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    direccion_envio = models.CharField(max_length=120)

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
