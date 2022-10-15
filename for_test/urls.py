from django.urls import path

from for_test.views import CategoryList, ProjectWeb, details_test_web, ProjectWebDetail, details, details_projet

urlpatterns = [
    path('test/liste-categories/', CategoryList.as_view(), name="list_categories"),
    path('test/projet-web/', ProjectWeb.as_view(), name="projet_web"),
    path('test/list-projet-web/<str:slug>/', details_projet, name="details_projet"),  # list of projects web
    path('test/details/<str:slug>/', ProjectWebDetail.as_view(), name='project_web_detail'),
    path('test/project/<str:slug>/', details, name='details'),
]
