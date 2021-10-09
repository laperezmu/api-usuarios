
from django.urls import path, include
from user.api.views import users_by_age, users_by_lastname, add_user, modify_user

urlpatterns = [
    path('list/age/', users_by_age, name='users-list-by-age'),
    path('list/lastname/', users_by_lastname, name='users-list-by-lastname'),
    path('add/', add_user, name='add-user'),
    path('<int:pk>/', modify_user, name='modify-or-delete-users'),
]
