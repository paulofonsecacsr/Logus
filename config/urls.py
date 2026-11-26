"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sobre.views import sobre
from equipe.views import equipe
from sr1.views import sr1
from sr2.views import sr2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sobre, name='sobre'),
    path('equipe/', equipe, name='equipe'),
    path('servicos/sr1/', sr1, name='sr1'),
    path('servicos/sr2/', sr2, name='sr2'),
]
