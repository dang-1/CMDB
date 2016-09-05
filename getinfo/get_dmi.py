#!/usr/bin/env python
#coding:utf-8
from subprocess import Popen, PIPE
def get_dmi():
    p = Popen(['dmidecode'], stdout=PIPE)
    return p.stdout.read()
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
def parseDmi(parsed_data):
    dic={}
    parsed_data = [ i for i in parsed_data if i.startswith('System Information')]
    parsed_data = [ i for i in parsed_data[0].split('\n')[1:] if i ]
    dmi_dic =  dict([ i.strip().split(':') for i in parsed_data ])
    dic['vender'] = dmi_dic['Manufacturer'].strip()
    dic['product'] = dmi_dic['Product Name'].strip()[:10]
    dic['sn'] = dmi_dic['Serial Number']
    return dic




if __name__ == "__main__":
    dmi_data = get_dmi()
    dmi_parse = parseData(dmi_data) 
    dmi =  parseDmi(dmi_parse)
    print dmi



