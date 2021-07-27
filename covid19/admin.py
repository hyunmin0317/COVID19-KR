from django.contrib import admin
from .models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    search_fields = ['date']

admin.site.register(Data, DataAdmin)