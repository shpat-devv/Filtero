from django.urls import path
from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('me/', UserProfileView.as_view(), name='user-delete'), 
    path('edit/', UserEditView.as_view(), name='user-password'),
]