from django.urls import path
from web.views import index, about, contacto, success, welcome

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contact'),
    path('exito/', success, name='success'),
]