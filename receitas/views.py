from django.shortcuts import render
from .Utils.receitas.factory import make_receitas

def Home(request):
    return render(request, 'receitas/Pages/home.html', context={
        'receitas':[make_receitas() for _ in range(10)]
    })

def Receita(request, id):
    receita = make_receitas()
    receita['id'] = id  # força o id da URL
    return render(request, 'receitas/Pages/Receitas-view.html', context={
        'receita': receita,
        'is_detail_page': True
    })
