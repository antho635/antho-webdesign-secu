from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def success_view(request):
    return HttpResponse("Success! Thank you for your message.")


# Index
def index(request):
    return render(request, 'portfolio/index.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')
