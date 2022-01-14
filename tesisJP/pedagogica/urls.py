from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PlanView


urlpatterns = [
    path('plan/', PlanView.as_view(), name="plan_list"),
  
]