from django.shortcuts import render
from django.views import generic

from for_test.models import Project


# fonction affiche les details du projet
class CategoryList(generic.ListView):
    model = Project
    queryset = Project.objects.all()
    template_name = 'forTest/list_category.html'


# Create your views here.
def test(request):
    return render(request, 'forTest/list_category.html')


def details_test_web(request):
    return render(request, 'forTest/details_test.html')
