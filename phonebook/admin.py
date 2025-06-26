from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'house_name', 'mobile')  # show these columns
    search_fields = ('name', 'mobile')               # enable search
    list_filter = ('house_name',)                    # add filter sidebar

admin.site.register(Contact, ContactAdmin)
