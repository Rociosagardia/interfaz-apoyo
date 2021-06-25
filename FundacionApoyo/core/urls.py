from django.urls import path
# from django.contrib import admin
from .views import usuarioDonadorRegistro,homePrincipal,inicioUsuario,iniciarSesion,donacion


urlpatterns = [
 
    path('', homePrincipal, name="homePrincipal"),
    path('usuarioDonadorRegistro/<action>/<id>', usuarioDonadorRegistro, name="usuarioDonadorRegistro"),

    
    path('iniciarSesion/', iniciarSesion, name="iniciarSesion"),
    path('inicioUsuario/<usuario>',inicioUsuario, name="inicioUsuario"),
    path('donacion/<action>/<id>',donacion,name="donacionUsuario")



]
