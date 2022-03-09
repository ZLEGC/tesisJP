from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from usuarios.models import User
from .forms import UsuarioForm
from .models import User
# Create your views here.



class UsuarioView(LoginRequiredMixin, generic.ListView):
    model =  User#modelo a utilizar 
    template_name= "u.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    login_url = "bases:login"



class CrearUsuarioView(LoginRequiredMixin, generic.CreateView):
    model =  User#modelo a utilizar 
    template_name= "crearU.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    form_class = UsuarioForm
    login_url = "bases:login"


class ActualizarUsuarioView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "actU.html"
    context_object_name = "obj"
    form_class = UsuarioForm
    login_url = "bases:login"


class BorrarUsuarioView(LoginRequiredMixin, generic.DeleteView):
    pass