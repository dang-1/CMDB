from django.contrib import admin
from hostinfo.models import Host, HostGroup
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
class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']
admin.site.register(Host, HostAdmin)
admin.site.register(HostGroup, HostGroupAdmin)
