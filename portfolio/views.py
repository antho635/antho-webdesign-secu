from django.shortcuts import render, get_object_or_404

from portfolio.models import Categorie, Project


def base(request):
    queryset = Project.objects.all().Category.objects.all()
    context = {
        'categorie_list': queryset,
        'project_list': queryset,
    }
    return render(request, 'portfolio/index.html', context)


# Index
def index(request):
    return render(request, 'portfolio/index.html')


def project_category(request):
    return render(request, 'portfolio/projets/category/project_category.html')


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

# Import Librariesfrom django.shortcuts
# import renderimport datetime
# Create your views here.def home(request):    currentdate = datetime.date.today()    formatDate = currentdate.strftime("%d-%b-%y")    return render(request,'home.html',                  {'current_date':currentdate,                   'format_date':formatDate} )