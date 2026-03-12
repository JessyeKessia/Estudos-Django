from django.urls import path
from . import views

urlpatterns = [
  path("welcome/", views.welcome, name="welcome"),
  path("eco/<str:text>/", views.eco),
  path("info/", views.info, name="info"),
  path("hora/", views.hora),
  path("login/", views.login),
  path("lista/", views.lista),
  path("home/", views.home, name="home"),
  path("contato/<str:telefone>/", views.contato, name="contato")
]