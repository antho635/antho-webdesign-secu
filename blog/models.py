from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    date_added = models.DateTimeField(auto_now=True, null=True, auto_created=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    # slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


STATUS = [
    (0, "Draft"),
    (1, "Publish")
]


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    thumbnail = models.ImageField(upload_to='images/blog/thumbnails/', default='images/blog/thumbnails/default.jpg')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("list_post", kwargs={"slug": self.slug})
