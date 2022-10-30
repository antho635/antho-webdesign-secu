from django.shortcuts import render


# Index
def index(request):
    return render(request, 'portfolio/index.html')


def project_category(request):
    return render(request, 'portfolio/projets/category/project_category.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')


def pizzeria(request):
    return render(request, 'portfolio/projets/pizzeria.html')
