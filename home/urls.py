from django.urls import path

from antho_webdesign.views import home

urlpatterns = [
    path('', home, name='home'),
]
