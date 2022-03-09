from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from academica.models import Grupo
# Create your views here.



class AcademicaView(LoginRequiredMixin, generic.ListView):
    model =  Grupo
    template_name= "indexA.html"
    context_object_name= "obj"
    login_url = "bases:login"