from rest_framework import serializers
from .models import PCSystemInfo

class PCSystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCSystemInfo
        fields = ['pc_name', 'cpu_usage', 'memory_usage', 'ram_total', 'ram_available', 'installed_apps']
