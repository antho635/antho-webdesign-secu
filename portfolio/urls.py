from django.urls import path

from portfolio.views import index, category_list, project_list, details_projet, base

urlpatterns = [
    path('', base, name='base'),
    path('', index, name='index_portfolio'),
    path('liste/categorie/', category_list, name='category_list'),
    path('liste/projets/', project_list, name='project_list'),
    path('details/projet/<slug:slug>/', details_projet, name='details_projet'),
]
