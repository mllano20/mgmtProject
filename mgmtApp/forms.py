from django import forms

from mgmtApp import models


class TareaForms(forms.ModelForm):
    class Meta:
        model = models.Tarea

        fields = [
            'idTarea',
            'proyecto',
            'team',
            'fechaIni',
            'fechaFin',
            'vehiculo',
            'descripcion',
            'observacion',
        ]
        field_order = {'idTarea',
                       'descripcion',
                       'fechaIni',
                       'fechaFin',
                       'team',
                       'proyecto',
                       'vehiculo',
                       'observacion', }

        labels = {
            'team': 'Team',
            'descripcion': 'Descripcion',
            'fechaIni': 'Fecha de Inicio',
            'fechaFin': 'Fecha de Finalizacion',
            'proyecto': 'Proyecto',
            'vehiculo': 'Vehiculo',
            'observacion': 'Observaciones'
        }

        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'input',
                                                 'rows': 5}),
            'observacion': forms.Textarea(attrs={'class': 'input',
                                                 'rows': 5}),
            'fechaIni': forms.DateInput(attrs={'class': 'input'}),
            'fechaFin': forms.DateInput(attrs={'class': 'input'}),

        }


class ProyectoForms(forms.ModelForm):
    class Meta:
        model = models.Proyecto

        fields = [
            'nombre',
            'cliente',
            'encargado',
            'tipo',
            'observacion',
        ]
        field_order = {'nombre',
                       'cliente',
                       'encargado',
                       'tipo',
                       'observacion', }

        labels = {
            'nombre': 'Nombre',
            'cliente': 'Cliente',
            'encargado': 'Encargado',
            'tipo': 'Tipo',
            'observacion': 'Observacion',
        }

        widgets = {

            'observacion': forms.Textarea(attrs={'class': 'input',
                                                 'rows': 5}),

        }


class ReporteSitioForms(forms.ModelForm):
    class Meta:
        fields = [
            'sitio',
            'tipo',
            'estacionCaptura',
            'observaciones',

        ]

        labels = {
            'sitio': 'Sitio',
            'tipo': 'Tipo',
            'estacionCaptura': 'Estaciones de Captura',
            'observaciones': 'Observaciones',

        }

        widgets = {
            'observaciones': forms.Textarea(attrs={'class': 'input',
                                                   'rows': 5}),

        }
