from django.urls import path
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/sobre.html'), name='sobre'),
    path('equipe/', TemplateView.as_view(template_name='core/equipe.html'), name='equipe'),
    path('sr1/', TemplateView.as_view(template_name='core/sr1.html'), name='sr1'),
    path('sr2/', TemplateView.as_view(template_name='core/sr2.html'), name='sr2'),
]