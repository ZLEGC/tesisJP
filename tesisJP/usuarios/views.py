from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from usuarios.models import User
# Create your views here.



class UsuarioView(LoginRequiredMixin, generic.ListView):
    model =  User#modelo a utilizar 
    template_name= "u.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    login_url = "bases:login"



class CrearUsuarioView(LoginRequiredMixin, generic.CreateView):
    pass


class ActualizarUsuarioView(LoginRequiredMixin, generic.UpdateView):
    pass


class BorrarUsuarioView(LoginRequiredMixin, generic.DeleteView):
    pass