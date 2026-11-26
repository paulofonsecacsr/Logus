from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def sobre(request):
    return render(request, 'core/sobre.html')

def equipe(request):
    return render(request, 'core/equipe.html')

def sr1(request):
    return render(request, 'core/sr1.html')

def sr2(request):
    return render(request, 'core/sr2.html')