# Generated by Django 4.1.1 on 2022-09-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='images/blog/thumbnails/default.jpg', upload_to='images/blog/thumbnails'),
        ),
    ]
