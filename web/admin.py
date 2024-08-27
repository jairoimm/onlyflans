from django.contrib import admin
from web.models import flan

# Register your models here.
class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(flan, FlanAdmin)