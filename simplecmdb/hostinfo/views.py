from django.shortcuts import render
from django.http import HttpResponse
from hostinfo.models import Host,HostGroup
import json
# Create your views here.
def collect(req):
    if req.POST:
        obj = json.loads(req.body)
        #hostname = req.POST.get('hostname')
        #print hostname
        #ip = req.POST.get('ip')
        #osver = req.POST.get('osver')
        #vendor = req.POST.get('vendor')
        #product = req.POST.get('product')
        #cpu_model = req.POST.get('cpu_model')
        #cpu_num = req.POST.get('cpu_num')
        #memory = req.POST.get('memory')
        #sn = req.POST.get('sn')
        hostname = obj['hostname']
        ip = obj['ip']
        osver = obj['osver']
        vendor = obj['vendor']
        product = obj['product']
        cpu_model = obj['cpu_model']
        cpu_num = obj['cpu_num']
        memory = obj['memory']
        sn = obj['sn']
        try:
            host = Host.objects.get(sn=sn)
        except:
            host = Host()
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
def getjson(req):
    ret_list = []
    hg = HostGroup.objects.all()
    for g in hg:
        ret = {'grouname':g.groupname,'members':[]}
        for h in g.members.all():
            ret_h = {'hostname':h.hostname,'ip':h.ip}
            ret['members'].append(ret_h)
        ret_list.append(ret)
    return HttpResponse(json.dumps(ret_list))
def gettxt(req):
    res = ''
    hg = HostGroup.objects.all()
    for g in hg:
        groupname = g.groupname
        for h in g.members.all():
            hostname = h.hostname
            ip = h.ip
            res += groupname+' '+hostname+' '+ip+'\n'
    return HttpResponse(res)
