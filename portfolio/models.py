from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=2500, blank=True, null=True)

    date_send = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_send']


# Create your models here.
CATEGORY_CHOICES = (
    ('site_web', 'Site Web'),
    ('appli_mobile', 'Appli Mobile'),
    ('appli_desktop', 'Appli Desktop'),
    ('other', 'Other'),
)

PROJECT_STATUS = (
    ('en_cours', 'En Cours'),
    ('en_ligne', 'En ligne'),
    ('canceled', 'Suspendu'),
)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_send']
    list_filter = ['date_send']
    ordering = ['-date_send']


# Create your models here.
CHOIX_CATEGORY = (
    ('site_web', 'Site Web'),
    ('appli_mobile', 'Appli Mobile'),
    ('appli_desktop', 'Appli Desktop'),
    ('other', 'Other'),
)

PROJET_STATUS = (
    ('en_cours', 'En Cours'),
    ('en_ligne', 'En ligne'),
    ('canceled', 'Suspendu'),
)


class Category(models.Model):
    category_name = models.CharField(max_length=120, blank=True, null=True)
    slug_category = models.SlugField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category_name']


class Project(models.Model):
    project_name = models.CharField(max_length=120, blank=True, null=True)
    slug_project = models.SlugField(max_length=120, blank=True, null=True)
    project_description = models.TextField(max_length=2500, blank=True, null=True)
    project_image = models.ImageField(upload_to='portfolio/images/', default='portfolio/images/default.png')
    project_link = models.URLField(max_length=200, blank=True, null=True)
    project_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    project_status = models.CharField(choices=PROJET_STATUS, default='en_cours', max_length=10)
    choix_category = models.CharField(choices=CHOIX_CATEGORY, default='site_web', max_length=20)
    project_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

    class Meta:
        ordering = ['project_name']
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

    def get_absolute_url(self):
        return reverse("project_details", kwargs={"slug": self.slug_project})


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'project_category', 'project_date']
    list_filter = ['project_date']
    ordering = ['-project_date']
