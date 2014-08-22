#!/usr/bin/env python
#encoding:utf-8

from get_address_by_ip import my_bin

def to10(item):
    ip_f, ip_t, ip_add = item.split("\t")
    ip_f = int("".join(map(my_bin,ip_f.split("."))),2)
    ip_t = int("".join(map(my_bin,ip_t.split("."))),2)
    return "\t".join([str(ip_f),str(ip_t),ip_add])

f = open("ip.txt")
data = f.readlines()
f.close()

f = open("my_ip.txt","w")
f.write("".join(map(to10,data)))
f.close()

