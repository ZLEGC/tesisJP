from django.urls import path
from django.urls.resolvers import URLPattern
from .views import AcademicaView


urlpatterns = [
    path('academiaca/', AcademicaView.as_view(), name="academica_list"),
    path('docente/', AcademicaView.as_view(), name="docente_list"),
]