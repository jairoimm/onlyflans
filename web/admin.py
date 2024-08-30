from django.contrib import admin
from web.models import flan, contact

# Register your models here.
class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(flan, FlanAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(contact, ContactAdmin)