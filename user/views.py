from django.shortcuts import render
from user.models import user
from django.http import JsonResponse

def users_by_age(request):
    users = user.objects.all()
    data = {
        'users':list(users.values())
        }
    return JsonResponse(data)
