from django.contrib import admin
from .models import Contact

# Register your models here.

# @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'list', 'date']
    # date_hierarchy = 'pub_date'


admin.site.register(Contact, ContactAdmin)
