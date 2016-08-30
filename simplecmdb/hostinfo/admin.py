from django.contrib import admin
from hostinfo.models import Host
# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname',
    'ip',
    'vendor',
    'product',
    'osver',
    'cpu_model',
    'cpu_num',
    'memory',
    'sn']
admin.site.register(Host, HostAdmin)
