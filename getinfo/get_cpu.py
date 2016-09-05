#!/usr/bin/env python
#coding:utf-8
from subprocess import Popen,PIPE
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


if __name__ == "__main__":
    print getCpu('/proc/cpuinfo')




