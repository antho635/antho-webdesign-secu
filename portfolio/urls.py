from django.urls import path

from portfolio.views import eco_demenagement, index, pizzeria, CategoryList, ProjectCategoryListe

urlpatterns = [
    path('', index, name='index_portfolio'),
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('projet/pizzeria/', pizzeria, name="pizzeria"),
    path('portfolio/categories/liste/', CategoryList.as_view(), name='list_category'),
    path('portfolio/category/projet/liste', ProjectCategoryListe.as_view(), name="projet_category_liste"),
    # path('portfolio/project/list/<slug:slug>/', ProjectListViewDetails.as_view(), name='project_details'),
    # path("contact/", contactView, name="contact"),
    # path("contact/", contact_form, name="contact_form"),
]
