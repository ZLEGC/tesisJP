from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UsuarioView


urlpatterns = [
    path('users/', UsuarioView.as_view(), name="users_list"),
  
]