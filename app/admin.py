from django.contrib import admin

# Register your models here.
from .models import BotUsers
@admin.register(BotUsers)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram','created']
    list_filter=['created']
    search_fields = ['name','telegram']
    list_per_page = 10