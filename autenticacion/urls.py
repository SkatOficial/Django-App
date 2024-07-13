from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.registrer, name="registrer"),
    path('signout', views.signout, name="signout"),
    path('signin', views.signin, name="signin"),
]