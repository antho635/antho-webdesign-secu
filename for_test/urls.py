from django.urls import path

from for_test.views import CategoryList, ProjectWeb, ProjectWebDetail, details, details_projet

urlpatterns = [
    path('t/liste-categories/', CategoryList.as_view(), name="list_categories"),
    path('t/liste/', ProjectWeb.as_view(), name="projet_web"),
    path('t/list-projet-web/<str:slug>/', details_projet, name="details_projet"),  # list of projects web
    path('t/categories/<str:slug>/', ProjectWebDetail.as_view(), name='project_web_detail'),
    path('t/projet/<str:slug>/details', details, name='details'),
]
