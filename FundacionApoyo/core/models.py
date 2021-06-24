from django.db import models

# Create your models here.

class TipoUsuarioDonador (models.Model):
    idTipoUsuarioDonador = models.AutoField(primary_key=True, verbose_name="Id de usuario donador")
    nombreTipoUsuarioDonador = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre del tipo de usuario Donador")

    def __str__(self):
        return self.nombreTipoUsuarioDonador

class MedioPago (models.Model):
    idMedioPago = models.AutoField(primary_key=True, verbose_name="Id Medio de pago")
    nombreTipoTarjeta = models.CharField(max_length=15, verbose_name="Nombre del tipo de Tarjeta")
    def __str__(self):
        return self.nombreTipoTarjeta

class UsuarioDonador (models.Model):
    rut = models.CharField(max_length=10, verbose_name="Rut")
    nombre = models.CharField(max_length=60, blank=False, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=60, null=True, blank=True, verbose_name="Apellido")
    email = models.CharField(max_length=60, null=True, blank=True,verbose_name="Email")
    nick = models.CharField(max_length=10,primary_key=True, blank=True,verbose_name="Nick")
    password = models.CharField(max_length=8, null=True, blank=True,verbose_name="Contraseña")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")    #/* la fecha viene del template*/
    MedioPago = models.ForeignKey (MedioPago, on_delete=models.DO_NOTHING)
    tipoUsuarioDonador = models.ForeignKey(TipoUsuarioDonador, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rut

class ingresoFundacion (models.Model):
    idIngresoFundacion = models.AutoField(primary_key=True, verbose_name="Id de Ingreso")
    MedioPago = models.ForeignKey(MedioPago, on_delete=models.DO_NOTHING)
    NumeroTarjeta = models.IntegerField(verbose_name="Numero de la tarjeta")
    monto = models.IntegerField(verbose_name="Monto del aporte")
    fecha_pago = models.DateField(verbose_name="Fecha del pago")
    UsuarioDonador = models.ForeignKey(UsuarioDonador, on_delete=models.DO_NOTHING)


class egresoFundacion (models.Model):
    idEgresoFundacion = models.AutoField(primary_key=True, verbose_name="Id Egreso fundacion")
    medio_pago_banco = models.CharField(max_length=60,verbose_name="Nombre del banco")
    tarjeta_banco = models.IntegerField(verbose_name="Tarjeta del Banco")
    monto_gasto = models.IntegerField(verbose_name="Monto del Gasto")
    descripccion_gasto = models.CharField(max_length=80, verbose_name="Descripcion del Gasto")
    fecha_gasto = models.DateField(verbose_name="Fecha del Gasto")