from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from user.api.serializers import UserSerializer
from user.models import User


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
def users_by_age(request):
    users = User.objects.all().order_by('edad')
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def users_by_lastname(request):
    users = User.objects.all().order_by('apellidoP')
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE', 'GET'])
def look_user(request, pk):
    users = User.objects.get(id = pk)

    if request.method == 'GET':
        serializer = UserSerializer(users)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        users.delete()
        return Response(status = HTTP_204_NO_CONTENT)
