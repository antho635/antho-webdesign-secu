# Generated by Django 4.1.1 on 2022-10-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_projectlist_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug_category', models.SlugField(blank=True, max_length=120, null=True)),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.AddField(
            model_name='projectlist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]
