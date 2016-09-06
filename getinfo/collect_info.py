#!/usr/bin/env python
#coding:utf-8
import urllib, urllib2
from subprocess import Popen,PIPE
import pickle
import json
import  platform
import time
def get_hostname():
    p = Popen(['uname','-a'],stdout=PIPE,stderr=PIPE)
    hostname = p.stdout.read().split()[1].strip()
    return {'hostname':hostname}
def get_system():
    system = platform.uname()[0]
    return {'system':system}
def get_osinfo():
    p = Popen(['cat','/etc/issue'],stdout=PIPE,stderr=PIPE)
    osinfo = p.stdout.readlines()[0].strip()
    #osinfo = os.popen("cat /etc/issue").readlines()[0].strip()
    return {'osinfo':osinfo}
def getCpu(f):
    num = 0
    with open(f) as fd:
        for line in fd:
            if line.startswith('processor'):
                num += 1
            if line.startswith('model name'):
                cpu_model = line.split(':')[1].split()
                cpu_model = cpu_model[0]+' '+cpu_model[-1]
    return {'cpu_num':num, 'cpu_model':cpu_model}
def getMemory(f):
    with open(f) as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                mem = int(line.split()[1].strip())
                break
    mem = "%s" %int((mem/1024.0))+'M'
    return {'memory_size':mem}
def get_external_ip():
    #p = Popen(['curl','ip.cip.cc'],stdout=PIPE,stderr=PIPE)
    #external_ip = p.stdout.read().strip()
    return {'external_ip':'1.1.1.1'}  #external_ip}
def getIfconfig():
    p = Popen(['ifconfig'],stdout=PIPE,stderr=PIPE)
    data = p.stdout.read()
    return data
def parseData(data):
    parsed_data = []
    new_line = ''
    data = [ i for i in data.split('\n') if i]
    for line in data:
        if line[0].strip():
            parsed_data.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    parsed_data.append(new_line)
    return [ i for i in parsed_data if i]
def parseIfconfig(parsed_data):
    dic = {}
    parsed_data = [ i for i in parsed_data if not i.startswith('lo')]
    for lines in parsed_data:
        line_list = lines.split('\n')
        #devname = line_list[0].split()[0]
        #macaddr = line_list[0].split()[-1]
        #ipaddr = line_list[1].split()[1].split(':')[1] #centos 6
        ipaddr = line_list[1].split()[1].split(':')[1]
        break
    dic['internal_ip1'] = ipaddr
    dic['internal_ip2'] = '0.0.0.0'
    return dic

if __name__ == '__main__':
    dic = {}
    hostname = get_hostname()
    system = get_system()
    osinfo =  get_osinfo()
    cpu_info =  getCpu('/proc/cpuinfo')
    mem_size = getMemory('/proc/meminfo')
    
    external_ip = get_external_ip()
    data_ip = getIfconfig()
    parsed_data_ip =  parseData(data_ip)
    internal_ip1 = parseIfconfig(parsed_data_ip)
    createdate = time.ctime()
    isdelete = 0
    dic['createdate'] = createdate
    dic['isdelete'] = isdelete
    dic.update(hostname)
    dic.update(system)
    dic.update(osinfo)
    dic.update(cpu_info)
    dic.update(mem_size)
    dic.update(external_ip)
    dic.update(internal_ip1)
    print dic
    d = json.dumps(dic)
    req = urllib2.urlopen('http://192.168.17.213:8000/hostinfo/collect/',d)
    print req.read()
