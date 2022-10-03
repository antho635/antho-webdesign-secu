from django.urls import path

from portfolio.views import eco_demenagement, index, pizzeria, project_list

urlpatterns = [
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('projet/pizzeria/', pizzeria, name="pizzeria"),
    path('portfolio/', index, name='index_portfolio'),
    path('portfolio/project/list/', project_list, name='project_list'),
    # path('portfolio/project/list/<slug:slug>/', ProjectListViewDetails.as_view(), name='project_details'),
    # path("contact/", contactView, name="contact"),
    # path("contact/", contact_form, name="contact_form"),
]
