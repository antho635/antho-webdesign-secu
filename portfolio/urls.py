from django.urls import path
from portfolio.views import eco_demenagement, index, contactView, successView, contact_form

urlpatterns = [
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('portfolio/', index, name='index_portfolio'),
    # path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    path("contact/", contact_form, name="contact_form"),
]
