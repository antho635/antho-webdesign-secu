from django.shortcuts import render
from django.views import generic

from portfolio.models import Project


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


# fonction affiche les details du projet
class ListCategory(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'portfolio/projets/category/list_category.html'


class ProjectSiteVitrine(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'portfolio/projets/category/list_site_vitrine.html'


class ProjectDetail(generic.DetailView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'portfolio/projets/category/details_projet.html'

