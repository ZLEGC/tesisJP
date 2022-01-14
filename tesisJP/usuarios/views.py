from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from usuarios.models import User
# Create your views here.



class UsuarioView(LoginRequiredMixin, generic.ListView):
    model =  User
    template_name= "u.html"
    context_object_name= "obj"
    login_url = "bases:login"