from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Autor, Editora, Livro
from .forms import AutorForm, EditoraForm, LivroForm

# Create your views here.
def welcome(request):
  return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
  return HttpResponse(f'Você digitou: {text}')


def hora(request):
  context = {
    "nome": "Jessye",
    "data": date.today()
  }
  # vai ser rederizado no home
  return render(request, "hora.html", context)

def login(request):
  context = {
    "is_logged_in": True,
    "role": "admin"
  }
  return render(request, "login.html", context)

def info(request):
  data = {
      "disciplina": "RAD",
      "framework": "Django",
      "semestre": "2026.1"
  }
  return JsonResponse(data)

def lista(request):
    produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 120},
        {"nome": "Teclado", "preco": 200},
    ]

    context = {
        "produtos": produtos
    }

    return render(request, "lista.html", context)

def home(request):
    return render(request, "home.html")

def contato(request, telefone):
    context = {
        "telefone": telefone
    }
    return render(request, "contato.html", context)

def home2(request):
    return render(request, 'home2.html')

# --- CRUD AUTOR ---
class AutorListView(ListView): model = Autor
class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('autor_list')
class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    success_url = reverse_lazy('autor_list')
class AutorDeleteView(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor_list')

# --- CRUD EDITORA ---
class EditoraListView(ListView): model = Editora
class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('editora_list')
class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    success_url = reverse_lazy('editora_list')
class EditoraDeleteView(DeleteView):
    model = Editora
    success_url = reverse_lazy('editora_list')

# --- CRUD LIVRO ---
class LivroListView(ListView): model = Livro
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('livro_list')
class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    success_url = reverse_lazy('livro_list')
class LivroDeleteView(DeleteView):
    model = Livro
    success_url = reverse_lazy('livro_list')