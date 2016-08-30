from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import Host
# Create your views here.
def collect(req):
    if req.POST:
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osver = req.POST.get('osver')
        vendor = req.POST.get('vendor')
        product = req.POST.get('product')
        cpu_model = req.POST.get('cpu_model')
        cpu_num = req.POST.get('cpu_num')
        memory = req.POST.get('memory')
        sn = req.POST.get('sn')
        host = Host()
        host.hostname = hostname
        host.ip = ip
        host.osver = osver
        host.vendor = vendor
        host.product = product
        host.cpu_model = cpu_model
        host.cpu_num = cpu_num
        host.memory = memory
        host.sn = sn
        host.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('no data')
