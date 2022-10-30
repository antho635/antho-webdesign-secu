# Generated by Django 4.1.1 on 2022-10-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0030_project_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug_category',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='description_cat',
            field=models.TextField(blank=True, max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image_cat',
            field=models.ImageField(blank=True, default='images/portfolio/category/default.jpg', null=True, upload_to='images/portfolio/category/'),
        ),
    ]