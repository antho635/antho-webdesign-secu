from django.contrib import admin
from django.urls import path, include
from antho_webdesign import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),
    # path('', include('for_test.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
