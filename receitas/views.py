from django.shortcuts import render


def Home(request):
    return render(request, 'receitas/Pages/home.html')

def Receitas(request,id):
    return render(request, 'receitas/Pages/Receitas-view.html')

