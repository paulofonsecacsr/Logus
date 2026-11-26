from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.sobre, name='sobre'),       # ajuste a rota raiz se necessário
    path('equipe/', views.equipe, name='equipe'),
    path('sr1/', views.sr1, name='sr1'),
    path('sr2/', views.sr2, name='sr2'),
]