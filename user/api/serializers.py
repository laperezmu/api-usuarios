
from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    nombre = serializers.CharField()
    apellidoP = serializers.CharField()
    apellidoM = serializers.CharField()
    edad = serializers.IntegerField()
    email = serializers.EmailField()
    telefono = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellidoP = validated_data.get('apellidoP', instance.apellidoP)
        instance.apellidoM = validated_data.get('apellidoM', instance.apellidoM)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.email = validated_data.get('email', instance.email)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.save()
        return instance