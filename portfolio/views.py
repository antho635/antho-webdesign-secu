from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "email.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")


def contact_form(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    date_send = request.POST.get('date_send')
    email = Contact.objects.create(name=name, email=email, message=message, date_send=date_send)
    email.save()

    return render(request, 'portfolio/contact/contactForm.html', {'email': email})


# Index
def index(request):
    return render(request, 'portfolio/index.html')


# Eco
def eco_demenagement(request):
    return render(request, 'portfolio/projets/eco-demenagement.html')
