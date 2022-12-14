# Generated by Django 4.1 on 2022-09-24 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_categories_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['-date_added'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
