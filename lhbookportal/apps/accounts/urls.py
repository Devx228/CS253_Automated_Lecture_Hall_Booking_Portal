from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView


app_name = 'accounts'

#  Helps with namespacing URLs using {% url 'accounts:login' %}

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]
