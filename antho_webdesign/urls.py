from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from for_test.views import test, details_test_web, CategoryList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),

    path('test/liste-categories/', CategoryList.as_view(), name="test"),
    path('test/', test, name='test'),
    path('test/details/<str:slug>/', details_test_web, name='details_test_web'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
