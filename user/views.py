# from django.shortcuts import render
# from user.models import user
# from django.http import JsonResponse

# def users_by_age(request):
#     users = user.objects.all().order_by('edad')
#     data = {
#         'users':list(users.values())
#         }
#     return JsonResponse(data)


# def users_by_lastname(request):
#     users = user.objects.all().order_by('apellidoP')
#     data = {
#         'users':list(users.values())
#         }
#     return JsonResponse(data)
