"""technical URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from technical.country.views import CountryViewSet
from technical.titulares.views import *

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet,'countries')
router.register(r'titulares', TitularesViewSet,'titulares')
router.register(r'titulares-fisicos', Titulares_Fisico_ViewSet,'titulares-fisicos')
router.register(r'titulares-juridicos', Titulares_Juridico_ViewSet,'titulares-juridicos')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
