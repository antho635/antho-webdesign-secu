from django.shortcuts import render

from django.views import generic

from .models import Post


def index_blog(request):
    return render(request, 'blog/index_blog.html')


def index_test(request):
    return render(request, 'blog/index_test.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/list_post.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class DevActus(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/developpement/list_post_dev.html'


class HackActus(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/hack/list_post_hack.html'


class CryptosActus(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/cryptos/list_post_cryptos.html'


class IaActus(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/ia/list_post_ia.html'


def dev_actus(request):
    return render(request, 'blog/developpement/list_post_dev.html')


class DevActusDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def hack_actus(request):
    return render(request, 'blog/hack/list_post_hack.html')


def cryptos_actus(request):
    return render(request, 'blog/cryptos/list_post_cryptos.html')


def ia_actus(request):
    return render(request, 'blog/ia/list_post_ia.html')
