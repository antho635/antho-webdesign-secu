from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    image_cat = models.ImageField(upload_to='images/portfolio/category',
                                  default='images/portfolio/category/default.jpg')
    description_cat = models.TextField(max_length=2500, blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category_name']
        verbose_name_plural = 'Categories'
        verbose_name = 'Categorie'

    def get_absolute_url(self):
        return reverse('list_categories', args=[self.slug])


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


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    project_status = models.CharField(choices=PROJECT_STATUS, default='en_cours', max_length=10)
    language_tags = models.CharField(max_length=50)
    project_thumbnail = models.ImageField(upload_to='images/portfolio/project/',
                                          default='images/portfolio/project/default.jpg')
    project_url = models.URLField(max_length=200, default='#')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category',
                                 blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

    def get_absolute_url(self):
        return reverse('project_web_detail', args=[self.slug])


class DetailsProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    details_project = models.TextField()

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name_plural = 'DetailsProjects'
        verbose_name = 'DetailsProject'
