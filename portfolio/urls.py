from django.urls import path
from portfolio.views import eco_demenagement, index, success_view

urlpatterns = [
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('portfolio/', index, name='index_portfolio'),
    # path("contact/", contactView, name="contact"),
    path("success/", success_view, name="success"),
    # path("contact/", contact_form, name="contact_form"),
]
