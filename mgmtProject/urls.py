"""mgmtProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from rest_framework import routers
from mgmtApp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Serializers define the API representation.

router = routers.DefaultRouter()
router.register('Cliente', views.ClienteView)
router.register('User', views.UserView)
router.register('Proyecto', views.ProyectView)

urlpatterns = [

    path('views/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^mgmtApp/', include('mgmtApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/toker/refresh', TokenRefreshView.as_view()),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
