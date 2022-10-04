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

# affichr les projets
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

