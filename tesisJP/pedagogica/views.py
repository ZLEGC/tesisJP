from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from pedagogica.models import Plan_Estudio
# Create your views here.



class PlanView(LoginRequiredMixin, generic.ListView):
    model =  Plan_Estudio
    template_name= "p.html"
    context_object_name= "obj"
    login_url = "bases:login"