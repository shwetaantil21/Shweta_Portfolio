from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']



