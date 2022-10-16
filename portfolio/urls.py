from django.urls import path

from portfolio.views import eco_demenagement, index, pizzeria, ListCategory, ProjectSiteVitrine

urlpatterns = [
    path('', index, name='index_portfolio'),
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('projet/pizzeria/', pizzeria, name="pizzeria"),
    path('liste-categories/', ListCategory.as_view(), name="list_categories"),
    path('projet-web/', ProjectSiteVitrine.as_view(), name="projet_site_vitrine"),
    # path('portfolio/project/list/<slug:slug>/', ProjectListViewDetails.as_view(), name='project_details'),
    # path("contact/", contactView, name="contact"),
    # path("contact/", contact_form, name="contact_form"),
]
