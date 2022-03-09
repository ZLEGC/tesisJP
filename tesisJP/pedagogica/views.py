import genericpath
from types import GenericAlias
from django.views import generic
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import fields
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.regex_helper import Group

from pedagogica.models import Plan_Estudio
from pedagogica.forms import PlanEstudioForm

# Create your views here.



class PlanView(LoginRequiredMixin, generic.ListView):
    model =  Plan_Estudio
    template_name= "p.html"
    context_object_name= "obj"
    login_url = "bases:login"

class CrearPlan(LoginRequiredMixin, generic.ListView):
   model = Plan_Estudio
   template_name= "crearplan.html"
   context_object_name= "obj"
   login_url = "bases:login"


