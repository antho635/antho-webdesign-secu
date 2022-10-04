from django.shortcuts import render
from django.views import generic


# Index
def index(request):
    return render(request, 'portfolio/index.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')


def pizzeria(request):
    return render(request, 'portfolio/projets/pizzeria.html')


def project_list(request):

    return render(request, 'portfolio/projets/project_list.html')
