# Generated by Django 4.1.1 on 2022-10-30 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('for_test', '0028_alter_project_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category_name',
        ),
    ]