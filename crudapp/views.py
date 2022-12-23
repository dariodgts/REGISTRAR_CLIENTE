from django.apps import apps
from django.db.models import F, ExpressionWrapper
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def crud(request):
    UsuarioListado = Usuario.objects.all()
    return render(request, "crud.html", {"Usuario": UsuarioListado})

def registrarUsuario(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    Año = request.POST['numAño']

    usuario = Usuario.objects.create(
        codigo=codigo, nombre=nombre, Año=Año)
    messages.success(request, '¡Usuario registrado!')
    return redirect('/')


def edicionUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    return render(request, "Añadir.html", {"usuario": usuario})


def editarUsuario(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    Año = request.POST['numAño']

    usuario = Usuario.objects.get(codigo=codigo)
    usuario.nombre = nombre
    usuario.Año = Año
    usuario.save()

    messages.success(request, '¡Usuario actualizado!')

    return redirect('/')


def eliminarUsuario(request, codigo):
    usuario = Usuario.objects.get(codigo=codigo)
    usuario.delete()

    messages.success(request, '¡Usuario eliminado!')

    return redirect('/')
