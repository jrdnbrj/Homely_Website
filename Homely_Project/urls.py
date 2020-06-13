"""Homely_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from apps.Homely.views.landing_page import *
from apps.Homely.views.admin import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.Homely.urls')),
    path('', landing_page, name = "landingPage"),
    path('login', iniciar_sesion, name = 'iniciar_sesión'),
    path('logout', cerrar_sesion, name = 'cerrar_sesión'),
    path('registrarUsuario', registrar_usuario, name = 'registrar_usuario'),
    path('administrar', administrar, name = 'administrar'),
    path('administrar/<str:model_name>/', administrar_tabla, name = 'administrar_tabla'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)