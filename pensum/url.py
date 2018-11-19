from django.conf.urls import url
from . import views



urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^pensum/nueva/$', views.grado_nueva, name='grado_nueva'),
    ]
