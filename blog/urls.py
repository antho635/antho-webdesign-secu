from django.urls import path
from .views import index_blog, PostDetail, PostList

urlpatterns = [
    path('blog/index/', index_blog, name="index_blog"),
    path('blog/', PostList.as_view(), name='list_post'),
    path('blog/post_detail/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
