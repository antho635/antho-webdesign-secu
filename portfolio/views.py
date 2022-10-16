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
class CategoryList(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'portfolio/projets/category/list_category.html'


class ProjectCategoryListe(generic.DetailView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'forTest/web/details_projet.html'


class project_list(generic.ListView):
    # queryset = Project.objects.filter(project_category__category_name='site vitrine')
    queryset = Project.objects.all()
    template_name = 'portfolio/projets/project_list.html'

# afficher les projets
# class ProjectListView(generic.ListView):
#     queryset = Project.objects.filter(status=1).order_by('-created_on')
#     template_name = 'portfolio/projets/project_list.html'

# afficher les details d'un projet
# class ProjectListViewDetails(generic.DetailView):
#     model = Project
#     template_name = 'portfolio/projets/project_details.html'

# def project_list(request):
#     return render(request, 'portfolio/projets/project_list.html')

# def project_details(request):
#     return render(request, 'portfolio/projets/project_details.html')
