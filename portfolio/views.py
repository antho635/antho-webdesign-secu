from django.shortcuts import render, get_object_or_404
from portfolio.models import Categorie, Project


def base(request):
    queryset_cat = Categorie.objects.all()
    return render(request, 'portfolio/index.html', {'categorie_list': queryset_cat})


# Index
def index(request):
    queryset_pro = Project.objects.all()
    return render(request, 'portfolio/index.html', {'project_list': queryset_pro})


def category_list(request):
    queryset = Categorie.objects.all()
    context = {
        'categorie_list': queryset
    }
    return render(request, 'portfolio/projets/category/list_category.html', context)


def project_list(request):
    queryset = Project.objects.all()
    context = {
        'project_list': queryset
    }
    return render(request, 'portfolio/projets/category/list_project.html', context)


def details_projet(request, slug):
    details_project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/projets/category/details_projet.html', {'details_project': details_project})
