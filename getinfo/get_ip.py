#!/usr/bin/env python
#coding:utf-8
# use in centos 6.x

from subprocess import Popen,PIPE


def get_internal_ip():
    new_line = ''
    lines = []
    dic = {}
    ip_inter = Popen(['ifconfig'],stdout=PIPE,stderr=PIPE)
    stdout,stderr = ip_inter.communicate()
    data = [i for i in stdout.split('\n') if i ]
    for line in data:
        if line[0].strip():
            lines.append(new_line)
            new_line = line + '\n'
        else:
            new_line += line + '\n'
    lines.append(new_line)
    all = [ i for i in lines if i and not i.startswith('lo')]
    for lines in all:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
        ipaddr = line_list[1].split()[1].split(':')[1]
        dic[devname] = ipaddr
    return dic

def get_external_ip():
    ip_e = Popen(['curl','ip.cip.cc'],stdout=PIPE,stderr=PIPE)
    ex_ip = ip_e.stdout.read().strip()
    return {"ex_ip":ex_ip}


if __name__ == '__main__':
    print get_external_ip()
    print get_internal_ip()



