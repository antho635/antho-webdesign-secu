# Generated by Django 4.1.1 on 2022-10-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0033_alter_project_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_cat',
            field=models.ImageField(blank=True, default='images/portfolio/category/default.jpg', null=True, upload_to='images/portfolio/category'),
        ),
    ]