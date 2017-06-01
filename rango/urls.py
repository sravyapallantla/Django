from django.conf.urls import url

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.index1, name='index1'),

]
