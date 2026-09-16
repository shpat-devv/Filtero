from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='user-create'),
    path('me/', User.as_view(), name='user-delete'), 
    path('password/me/', UserPasswordUpdateView.as_view(), name='user-password'),
]