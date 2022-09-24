from django.urls import path

from .views import PostDetail, PostList, index_test, index_blog, dev_actus, hack_actus, cryptos_actus, ia_actus, \
    DevActus, DevActusDetail, HackActus, CryptosActus, IaActus

urlpatterns = [
    path('blog/', index_blog, name="index_blog"),
    path('blog/test', index_test, name="index_test"),
    path('blog/list/', PostList.as_view(), name='list_post'),

    path('blog/list/developpement/', DevActus.as_view(), name='list_post_dev'),
    path('blog/list/<slug:slug>/', DevActusDetail.as_view(), name='post_detail_dev'),

    path('blog/list/cybersecurite/', HackActus.as_view(), name='list_post_hack'),

    path('blog/list/cryptomonnaie/', CryptosActus.as_view(), name='list_post_cryptos'),

    path('blog/list/i-a/', IaActus.as_view(), name='list_post_ia'),

    # path('blog/list/hacking', hack_actus, name='list_post_hack'),
    # path('blog/list/cryptos', cryptos_actus, name='list_post_cryptos'),
    # path('blog/list/ia', ia_actus, name='list_post_ia'),
    path('blog/post_detail/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
