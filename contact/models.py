from django.contrib import admin
from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi", null=True)

    def __str__(self):
        return self.email


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'date_envoye']
    list_filter = ['date_envoye']
    ordering = ['-date_envoye']
