# Generated by Django 4.1 on 2022-09-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_date_envoye'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
