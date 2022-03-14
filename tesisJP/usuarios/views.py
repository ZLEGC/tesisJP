from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from usuarios.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy
from .models import User
from django.shortcuts import get_object_or_404
# Create your views here.



class UsuarioView(LoginRequiredMixin, generic.ListView):
    model =  User#modelo a utilizar 
    template_name= "u_list.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    login_url = "bases:login"



class CrearUsuarioView(LoginRequiredMixin, generic.CreateView):
    model =  User#modelo a utilizar 
    template_name= "crearU.html"#nombre del template a utilizar 
    context_object_name= "obj"#es un objeto deonde podemos guardar info que vamos hacer llegar al template
    form_class = UsuarioForm
    succes_url = reverse_lazy("usuarios:usuarios_list")
    login_url = "bases:login"
    def form_valid(self, form):
        form.instance.uc = self.request.user
        form.save()
        return HttpResponseRedirect(reverse_lazy('usuarios:user_list'))

class ActualizarUsuarioView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "crearU.html"
    context_object_name = "obj"
    form_class = UsuarioForm
    login_url = "bases:login"


class BorrarUsuarioView(LoginRequiredMixin, generic.DeleteView):
    pass