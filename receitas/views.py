from django.shortcuts import render


def Home(request):
    return render(request, 'receitas/Pages/home.html')
