from django.contrib.auth.models import User
from django.shortcuts import render
from mgmtApp import forms
from django.contrib import messages

from .models import Team, Cliente, Proyecto, Vehiculo, Tarea
from .serializer import ClienteSerializer, UserSerializer, ProyectoSerializer
from rest_framework import viewsets, permissions


def index(request):
    current_user = request.user
    clientes = Cliente.objects.all()
    users = User.objects.all()
    team = Team.objects.filter(usuarios=current_user)
    args = {'users': users, 'teams': team, 'clientes': clientes}

    return render(
        request,
        'index.html',
        args,
    )


def clientes(request):
    current_user = request.user
    lclientes = Cliente.objects.all()
    users = User.objects.all()
    team = Team.objects.filter(usuarios=current_user)
    args = {'users': users, 'teams': team, 'clientes': lclientes}

    return render(
        request,
        'clientes.html',
        args,
    )


# Funciones para manipulacion de proyectos


def proyectos(request, pk=None):
    if pk:
        proyecto = Proyecto.objects.get(pk=pk)
        tareas = Tarea.objects.filter(proyecto__id=pk)
        encargado = proyecto.encargado
        args = {'proyecto': proyecto, 'tareas': tareas, 'encargado': encargado}

        return render(
            request,
            'proyecto.html',
            args, )
    else:
        current_user = request.user
        lproyectos = Proyecto.objects.all()
        users = User.objects.all()
        team = Team.objects.filter(usuarios=current_user)
        args = {'users': users, 'teams': team, 'proyectos': lproyectos}

        return render(
            request,
            'proyectos.html',
            args, )


def proyectos_edit(request, pk):
    proyecto_pk = Proyecto.objects.get(pk=pk)
    form = forms.ProyectoForms(instance=proyecto_pk)
    if request.method == 'POST':
        form = forms.ProyectoForms(instance=proyecto_pk, data=request.POST)
        if form.is_valid():
            proyectoF = form.save(commit=False)
            form.save()
            return proyectos(request)

    context = {'form': form}
    return render(
        request,
        'proyecto_edit.html',
        context
    )


def proyectos_crear(request):
    if request.method == 'POST':
        form = forms.ProyectoForms(data=request.POST)
        if form.is_valid():
            proyectoF = form.save(commit=False)
            form.save()
            pk = proyectoF.pk
            return proyectos(request, pk)

    context = {'form': form}
    return render(
        request,
        'proyecto_edit.html',
        context
    )

# Funciones para manipulacion de tareas


def tarea(request, pk):
    tarea_pk = Tarea.objects.get(idTarea=pk)
    args = {'tarea': tarea_pk}
    return render(
        request,
        'tarea.html',
        args,
    )


def tarea_edit(request, pk):
    tarea_pk = Tarea.objects.get(idTarea=pk)
    form = forms.TareaForms(instance=tarea_pk)
    if request.method == 'POST':
        form = forms.TareaForms(instance=tarea_pk, data=request.POST)
        if form.is_valid():
            tareaF = form.save(commit=False)
            form.save()
            return tarea(request, pk)

    context = {'form': form}
    return render(
        request,
        'tarea_edit.html',
        context
    )


def tarea_crear(request):
    form = forms.TareaForms()
    if request.method == 'POST':
        form = forms.TareaForms(data=request.POST)
        if form.is_valid():
            tareaF = form.save(commit=False)
            form.save()
            pk = tareaF.idTarea
            return tarea(request, pk)

    context = {'form': form}
    return render(
        request,
        'tarea_edit.html',
        context
    )


def tarea_delete(request, pk):
    tarea_pk = Tarea.objects.get(idTarea=pk)
    proyecto_tarea = tarea_pk.proyecto
    tarea_pk.delete()
    return proyectos(request, proyecto_tarea.pk)


def vehiculos(request):
    current_user = request.user
    lvehiculos = Vehiculo.objects.all()
    users = User.objects.all()
    team = Team.objects.filter(usuarios=current_user)
    args = {'users': users, 'teams': team, 'vehiculos': lvehiculos}

    return render(
        request,
        'vehiculos.html',
        args,
    )

# Funciones para manipulacion de reportes de sitios


def reportesitios_crear(request):
    form = forms.ReporteSitioForms()
    if request.method == 'POST':
        form = forms.ReporteSitioForms(data=request.POST)
        if form.is_valid():
            rep_sitio = form.save(commit=False)
            form.save()
            pk = rep_sitio.idTarea

    context = {'form': form}
    return render(
        request,
        'tarea_edit.html',
        context
    )


class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAdminUser


class ProyectView(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


def login(request):
    return render(
        request,
        'login.html',
    )
