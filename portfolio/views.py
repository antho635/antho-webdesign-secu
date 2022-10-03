from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import ContactForm
from .models import Contact, ProjectList


# Index
def index(request):
    return render(request, 'portfolio/index.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')


def pizzeria(request):
    return render(request, 'portfolio/projets/pizzeria.html')


class ProjectListView(generic.ListView):
    queryset = ProjectList.objects.order_by('-project_date_created_on')
    template_name = 'portfolio/projets/project_list.html'


def project_list(request):
    return render(request, 'portfolio/projets/project_list.html')
