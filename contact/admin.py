from django.contrib import admin
from .models import Contact, ContactAdmin

admin.site.register(Contact, ContactAdmin)
