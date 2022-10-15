from django.db import models
from django.urls import reverse

# Create your models here.
CATEGORY_CHOICES = (
    (0, 'Web'),
    (1, 'Mobile'),
    (2, 'Desktop'),
    (3, 'Other'),
)

PROJECT_STATUS = (
    (0, 'en_cours'),
    (1, 'En ligne'),
    (2, 'Suspendu'),
)


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    project_status = models.IntegerField(choices=PROJECT_STATUS, default=0)
    language_tags = models.CharField(max_length=50)
    project_thumbnail = models.ImageField(upload_to='images/portfolio/project/',
                                          default='images/portfolio/project/default.png')
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    project_url = models.URLField(max_length=200, default='#')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'

    def get_absolute_url(self):
        return reverse('details_test_web', args=[self.slug])


class DetailsProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    details_project = models.TextField()

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name_plural = 'DetailsProjects'
        verbose_name = 'DetailsProject'
