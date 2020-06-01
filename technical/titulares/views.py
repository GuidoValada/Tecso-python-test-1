
from rest_framework import viewsets
from rest_framework import permissions
from .models import Titulares
from .serializers import *




class TitularesViewSet(viewsets.ModelViewSet):
    queryset = Titulares.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TitularesSerializer
  


class Titulares_Fisico_ViewSet(viewsets.ModelViewSet):
    queryset = Titulares.objects.filter(tipo_titular__iexact= 'fisico').order_by('nombre')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = titulares_fisico_serializer

class Titulares_Juridico_ViewSet(viewsets.ModelViewSet):
    queryset = Titulares.objects.filter(tipo_titular__iexact = 'juridico').order_by('razon_social')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = titulares_juridico_serializer


    