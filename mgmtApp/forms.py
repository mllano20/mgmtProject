from django import forms

from mgmtApp import models
from django.utils.translation import ugettext_lazy as _


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
