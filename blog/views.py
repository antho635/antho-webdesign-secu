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
