from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=50, default='')

    def __str__(self):
        return (self.nombre)

class Localidad(models.Model):
    nombre = models.CharField(max_length=50, default='')
    provincia = models.ForeignKey(Provincia, on_delete= models.PROTECT, null=True)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=200, default='')
    piso = models.CharField(max_length=10, default=0, null=True)
    numero = models.CharField(max_length=10, default=0, null=True)
    provincia = models.ForeignKey(Provincia, on_delete= models.PROTECT, null=True)
    localidad = models.ForeignKey(Localidad, on_delete= models.PROTECT, null=True)

    def __str__(self):
        return "{} Piso: {} Numero: {}".format(self.direccion, self.piso, self.numero)

class Inquilino(models.Model):
    dni= models.IntegerField()
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    celular = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    departamento = models.ForeignKey(Departamento, on_delete= models.PROTECT, null=True)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)

class Contrato(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete= models.PROTECT, null=True)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.PROTECT, null=True)
    fechaContrato_inicio= models.DateField(null=True)
    fechaContrato_fin= models.DateField(null=True)
    fecha_vencimiento= models.DateField(null=True)

    def __str__(self):
        return "Desde: {} Hasta: {}".format(self.fechaContrato_inicio, self.fechaContrato_fin)

class Concepto(models.Model):
    nombre= models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
class Pagos(models.Model):
    numero= models.CharField(max_length=15)
    inquilino = models.ForeignKey(Inquilino, on_delete=models.PROTECT, null=True)
    fecha= models.DateTimeField(auto_now_add=True)
    monto= models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # vencimiento= models.DateField()
    pago_mes= models.CharField(max_length=20, null=True)
    concepto = models.CharField(max_length=20, default='Alquiler')
    nota= models.CharField(max_length=50, null=True)

    def __str__(self):
        return "{} {} {}".format(self.fecha, self.monto, self.monto)

class Factura(models.Model):
    pass



