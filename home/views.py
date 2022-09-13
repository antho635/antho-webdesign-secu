from django.shortcuts import render
from django.http import HttpResponseRedirect

from portfolio.forms import ContactForm


def home(request):
    return render(request, "home/home.html")
