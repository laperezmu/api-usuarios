#Django rest framework imports
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

#Internal imports
from user.api.serializers import UserSerializer
from user.models import User


#Create - add a new user method
@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


#Read - get all users info in a disordered list
@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


#Read - get all users info in a list ordered by "Edad"
@api_view(['GET'])
def users_by_age(request):
    users = User.objects.all() #Podría ser users = User.objects.all().order_by('edad')
    serializer = UserSerializer(users, many = True)
    items = serializer.data
    query_returned = sorted(items, key=lambda d: d['edad']) 
    return Response(query_returned)


#Read - get all users infor in a list ordered by "Apellido parterno"
@api_view(['GET'])
def users_by_lastname(request):
    users = User.objects.all() #Podría ser users = User.objects.all().order_by('apellidoP')
    serializer = UserSerializer(users, many = True)
    items = serializer.data
    query_returned = sorted(items, key=lambda d: d['apellidoP']) 
    return Response(query_returned)


#Read, Update and Delete - look for a user by ID and depents on the HTTP method applies an update, a read of the user's info or delete the user
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
