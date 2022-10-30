from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404
from django.views import generic

from for_test.models import Project, Category


# fonction affiche les details du projet
class CategoryList(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'forTest/list_category.html'


class ProjectWeb(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'forTest/web/list_category_web.html'


class ProjectWebDetail(generic.DetailView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'forTest/web/details_projet.html'


def details_projet(request, slug):
    details_project = get_object_or_404(Project, slug=slug)
    return render(request, 'forTest/web/details_projet.html', {'details_project': details_project})


def details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'forTest/web/details_projet.html', {'project': project})
