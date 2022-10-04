# Generated by Django 4.1.1 on 2022-10-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200, unique=True)),
                ('project_slug', models.SlugField(max_length=200, unique=True)),
                ('project_description', models.TextField()),
                ('project_date_created_on', models.DateTimeField(auto_now_add=True)),
                ('project_status', models.IntegerField(choices=[(0, 'En cours'), (1, 'En ligne')], default=0)),
                ('language_tags', models.CharField(max_length=50)),
                ('project_thumbnail', models.ImageField(default='images/portfolio/project/indispo.png', upload_to='images/portfolio/project/')),
            ],
            options={
                'ordering': ['-project_date_created_on'],
            },
        ),
    ]