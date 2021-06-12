from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=200, default='')
    piso = models.CharField(max_length=10, default=0, null=True)
    numero = models.CharField(max_length=10, default=0, null=True)
    proxVenc= models.DateField(null= True) #temporal
    def __str__(self):
        return "{} Piso: {} Numero: {}".format(self.direccion, self.piso, self.numero)

class Inquilino(models.Model):
    dni= models.IntegerField()
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    celular = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    fechaContrato_inicio= models.DateField(null= True)
    fechaContrato_fin= models.DateField(null= True)
    departamento = models.ForeignKey(Departamento, on_delete= models.PROTECT, null=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Pagos(models.Model):
    numero= models.CharField(max_length=15)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.PROTECT, null=True)
    fecha= models.DateTimeField(auto_now_add=True)
    monto= models.DecimalField(max_digits=8, decimal_places=2, default=0)
    vencimiento= models.DateField()

    def __str__(self):
        return "{} {} {}".format(self.fecha, self.monto, self.monto)

#class Cuenta(models.Model):

class Factura(models.Model):
    pass



