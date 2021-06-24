from django.contrib import admin
from .models import TipoUsuarioDonador,MedioPago,UsuarioDonador,ingresoFundacion,egresoFundacion
# Register your models here.

admin.site.register(TipoUsuarioDonador)
admin.site.register(MedioPago)
admin.site.register(UsuarioDonador)
admin.site.register(ingresoFundacion)
admin.site.register(egresoFundacion)
