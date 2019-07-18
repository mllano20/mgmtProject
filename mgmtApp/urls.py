from django.conf.urls import url
from django.urls import include, path

from mgmtApp.loginForm import LoginForm
from . import views
from rest_framework import routers


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clientes$', views.clientes, name='clientes'),
    url(r'^proyectos$', views.proyectos, name='proyectos'),
    url(r'^proyectos/(?P<pk>\d+)$', views.proyectos, name='proyectos_pk'),
    path('tarea/P<pk>', views.tarea, name='tarea'),
    path('tarea/edit/P<pk>', views.tarea_edit, name='tarea_edit'),
    path('tarea/edit', views.tarea_crear, name='tarea_crear'),
    url(r'^vehiculos$', views.vehiculos, name='vehiculos'),
    url(r'^login/', views.login, {'authentication_form': LoginForm}, name='login'),
    url(r'^api-auth/', include('rest_framework.urls')),
]

