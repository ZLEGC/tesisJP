from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AcademicaView


urlpatterns = [
    path('docentes/', AcademicaView.as_view(), name="docentes_list"),
  
]