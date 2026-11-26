from django.shortcuts import render

# Create your views here.

def equipe(request):
    return render(request, 'equipe/equipe.html')
    