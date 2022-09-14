from django.urls import path

from .views import PostDetail, PostList, index_test, index_blog

urlpatterns = [
    path('blog/', index_blog, name="index_blog"),
    path('blog/test', index_test, name="index_test"),
    path('blog/list', PostList.as_view(), name='list_post'),
    path('blog/post_detail/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
