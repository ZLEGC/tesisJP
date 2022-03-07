from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PlanView, CrearPlan


urlpatterns = [
    path('plan/', PlanView.as_view(), name="plan_list"),
    path('CrearPlan/', CrearPlan.as_view(),name='crear_plan')
  
]
