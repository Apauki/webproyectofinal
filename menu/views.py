from django.shortcuts import render
from .models import Menu, TipoMenu

# Create your views here.

def tipoMenu(request):
    tipoMenu = TipoMenu.objects.all()
    return render(request, "menu/tipo.html", {'menus': menus})

def menu(request):
    menus = Menu.objects.all()
    return render(request, "menu/menu.html", {'menus': menus})