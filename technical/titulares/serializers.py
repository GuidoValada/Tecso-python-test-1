from rest_framework import serializers
from technical.titulares.models import Titulares
from operator import itemgetter
from collections import OrderedDict


class TitularesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Titulares
        fields = ['nombre','apellido','dni','tipo_titular','cuit','año_fundacion','razon_social','id']

    def validate(self, data):
        if data['tipo_titular'].lower() == 'fisico':
            if not data['nombre']:
                raise serializers.ValidationError({"Error": ("Nombre es un campo requerido.")})
            if not data['apellido']:
                raise serializers.ValidationError({"Error": ("Apellido es un campo requerido.")})
            if not data['dni']:
                raise serializers.ValidationError({"Error": ("Dni es un campo requerido.")})
            data['tipo_titular'] = 'fisico'
            data['razon_social'] = None
            data['año_fundacion'] = None
        elif data['tipo_titular'].lower() == 'juridico':
            if not data['año_fundacion']:
                raise serializers.ValidationError({"Error": ("Año de fundacion es un campo requerido.")})
            if len(data['año_fundacion']) < 4:
                raise serializers.ValidationError({'Error': ("El año de fundacion debe ser de 4 digitos.")})
            if not data['razon_social']:
                raise serializers.ValidationError({"Error": ("Razon social es un campo requerido.")})
            data['tipo_titular'] = 'juridico'
            data['nombre'] = None
            data['apellido'] = None
            data['dni']= None
        else:
            raise serializers.ValidationError({"Error:": ("El tipo de titular es incorrecto.")})
        
        return data


    def to_representation(self, instance):
        #Eliminar los campos sin datos en las GET REQUEST.
        ret = super().to_representation(instance)
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret


class titulares_fisico_serializer(serializers.ModelSerializer):
    tipo_titular = serializers.CharField(read_only=True)
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    dni = serializers.IntegerField()
    class Meta:
        model = Titulares
        fields = ['nombre','apellido','dni','tipo_titular','cuit']
    
    def validate(self, data):
        data['tipo_titular'] = 'fisico'
        return data    
    
    
    
class titulares_juridico_serializer(serializers.ModelSerializer):
    tipo_titular = serializers.CharField(read_only=True)
    razon_social = serializers.CharField()
    class Meta:
        model = Titulares
        fields = ['año_fundacion','razon_social','tipo_titular','cuit']
    
    def validate(self, data):
        data['tipo_titular'] = 'juridico'
        if len(data['año_fundacion']) < 4:
            raise serializers.ValidationError({'Error': ("El año de fundacion debe ser de 4 digitos.")})
        return data    
    
   
         


        
        
