# Register your models here.
from django.contrib import admin
from .models import PCSystemInfo

@admin.register(PCSystemInfo)
class PCSystemInfoAdmin(admin.ModelAdmin):
    list_display = ['pc_name', 'cpu_usage', 'memory_usage', 'ram_total', 'ram_available']
    list_filter = ['pc_name']
    search_fields = ['pc_name']
