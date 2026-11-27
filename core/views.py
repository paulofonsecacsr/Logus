from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# As quatro páginas atuais são estáticas (sem dados de banco), então usam
# TemplateView direto em core/urls.py. Crie uma view aqui só quando uma
# página precisar de lógica própria (formulário, consulta ao banco, etc.).