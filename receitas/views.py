from django.shortcuts import render
from django.http import Http404
from .Utils.receitas.factory import make_receitas

# Simula um "banco de dados" em memória
receitas_db = [make_receitas() for _ in range(50)]

def Home(request):
    return render(request, 'receitas/Pages/home.html', {
        'receitas': receitas_db[:10]
    })

def Receita(request, id):
    receita = next((r for r in receitas_db if r['id'] == id), None)
    if receita is None:
        raise Http404("Receita não encontrada")
    return render(request, 'receitas/Pages/Receitas-view.html', {
        'receita': receita,
        'is_detail_page': True
    })

def search(request):
    query = request.GET.get('search', '')
    resultados = [r for r in receitas_db if query.lower() in r['title'].lower()]
    return render(request, 'receitas/Pages/home.html', {
        'receitas': resultados
    })
