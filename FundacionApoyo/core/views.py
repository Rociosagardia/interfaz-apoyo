from django.shortcuts import render
from .models import UsuarioDonador
from .forms import UsuarioDonadorForm, DonacionForm


def homePrincipal(request):
    return render(request, "core/homePrincipal.html")


def usuarioDonadorRegistro(request, action, id):
    data = {"mesg": "", "form": UsuarioDonadorForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = UsuarioDonadorForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El usuario fue creado correctamente!"
                except:
                    data["mesg"] = "¡El usuario ya esta registrado!"
    return render(request, "core/usuarioDonadorRegistro.html", data)


def iniciarSesion(request):
    return render(request, 'core/iniciar_sesion.html')


def inicioUsuario(request, usuario):

    usuario = UsuarioDonador.objects.get(nick=usuario)
    data = {"usuario": usuario}
    data["mesg"] = "¡El usuario fue encontrado!"
    return render(request, 'core/inicio_usuario.html', data)


def donacion(request, action, id):
    data = {"mesg": "", "form": DonacionForm, "action": action, "id": id}

    if action == 'ins':
        if request.method == "POST":
            form = DonacionForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡La donacion fue enviada correctamente!"
                except:
                    data["mesg"] = "¡La donacion no pudo ser enviada!"
    return render(request, 'core/donacion.html', data)
