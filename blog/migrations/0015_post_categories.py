# Generated by Django 4.1 on 2022-09-24 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_post_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
