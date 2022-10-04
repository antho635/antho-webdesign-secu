from django.urls import path

from portfolio.views import eco_demenagement, index, pizzeria, project_list, project_category

urlpatterns = [
    path('projet/eco_demenagement/', eco_demenagement, name="eco-demenagement"),
    path('projet/pizzeria/', pizzeria, name="pizzeria"),
    path('', index, name='index_portfolio'),
    path('project/list/', project_list.as_view(), name='project_list'),
    path('project/category/list/', project_category, name='project_category'),
    # path('portfolio/project/list/<slug:slug>/', ProjectListViewDetails.as_view(), name='project_details'),
    # path("contact/", contactView, name="contact"),
    # path("contact/", contact_form, name="contact_form"),
]
