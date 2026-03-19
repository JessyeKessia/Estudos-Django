from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

# Create your views here.
def welcome(request):
  return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
  return HttpResponse(f'Você digitou: {text}')

# request com o meu nome
def hora(request):
  # envia as variáveis como contexto para ser rederizado
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