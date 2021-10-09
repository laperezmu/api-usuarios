
from django.urls import path, include

from user.views import users_by_age

urlpatterns = [
    path('list/age/', users_by_age, name='users-list-by-age')
]
