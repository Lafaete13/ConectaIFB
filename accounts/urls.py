from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('accounts/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('accounts/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-destroy'),
]