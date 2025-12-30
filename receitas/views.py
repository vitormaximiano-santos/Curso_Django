from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'receitas/home.html')

def Contatos(request):
    return HttpResponse('Contatos')

def Sobre(request):
    return HttpResponse('Sobre')

def conteudo(request):
    return HttpResponse('Conteúdo de receitas')