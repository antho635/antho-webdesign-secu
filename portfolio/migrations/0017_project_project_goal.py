# Generated by Django 4.1.3 on 2022-11-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_project_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_goal',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]