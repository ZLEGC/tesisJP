from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UsuarioView,CrearUsuarioView,ActualizarUsuarioView,BorrarUsuarioView


urlpatterns = [
    path('usuario/', UsuarioView.as_view(), name="users_list"),
    path('usuariocrear/', CrearUsuarioView.as_view(), name="users_crear"),
    path('usuarioactualizar/<int:pk>', ActualizarUsuarioView.as_view(), name="users_actualizar"),
    path('usuarioborrar/<int:pk>', BorrarUsuarioView.as_view(), name="users_borrar"),  
  
]