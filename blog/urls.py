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
  path("contato/<str:telefone>/", views.contato, name="contato"),
  path('', views.home2, name='home2'),
   # Autor
  path('autores/', views.AutorListView.as_view(), name='autor_list'),
  path('autores/novo/', views.AutorCreateView.as_view(), name='autor_create'),
  path('autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='autor_update'),
  path('autores/deletar/<int:pk>/', views.AutorDeleteView.as_view(), name='autor_delete'),

  # Editora
  path('editoras/', views.EditoraListView.as_view(), name='editora_list'),
  path('editoras/novo/', views.EditoraCreateView.as_view(), name='editora_create'),
  path('editoras/editar/<int:pk>/', views.EditoraUpdateView.as_view(), name='editora_update'),
  path('editoras/deletar/<int:pk>/', views.EditoraDeleteView.as_view(), name='editora_delete'),

  # Livro
  path('livros/', views.LivroListView.as_view(), name='livro_list'),
  path('livros/novo/', views.LivroCreateView.as_view(), name='livro_create'),
  path('livros/editar/<int:pk>/', views.LivroUpdateView.as_view(), name='livro_update'),
  path('livros/deletar/<int:pk>/', views.LivroDeleteView.as_view(), name='livro_delete'), 
]