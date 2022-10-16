# Generated by Django 4.1.1 on 2022-10-16 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_project_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['project_name'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='slug_projects',
            new_name='slug_project',
        ),
        migrations.AddField(
            model_name='project',
            name='choix_category',
            field=models.CharField(choices=[('site_web', 'Site Web'), ('appli_mobile', 'Appli Mobile'), ('appli_desktop', 'Appli Desktop'), ('other', 'Other')], default='site_web', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]
