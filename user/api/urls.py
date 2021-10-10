#Django imports
from django.urls import path, include

#Internal imports
from user.api.views import users_by_age, users_by_lastname, add_user, look_user, users_list


#URLS

urlpatterns = [
    path('', users_list, name='users-list'),
    path('order-by-age/', users_by_age, name='users-list-by-age'),
    path('order-by-lastname/', users_by_lastname, name='users-list-by-lastname'),
    path('add/', add_user, name='add-user'),
    path('<int:pk>/', look_user, name='modify-or-delete-users'),
]
