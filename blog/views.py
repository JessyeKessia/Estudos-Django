from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def welcome(request):
  return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
  return HttpResponse(f'Você digitou: {text}')

def info(request):
  data = {
      "disciplina": "RAD",
      "framework": "Django",
      "semestre": "2026.1"
  }
  return JsonResponse(data)
