#!/usr/bin/env python
#encoding:utf8

import sys

def my_bin(oct_num):
    result = bin(int(oct_num))[2:]
    if len(result) == 8:
        return result
    else:
        return "0"*(8-len(result)) + result

def get_address(ip):
    ip_to10 = int("".join(map(my_bin,ip.split("."))),2)
    if ip_to10 > 4294967295:
        return -1
    high = len(data) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        midVal = data[mid]
        if int(midVal.split()[1]) < ip_to10:
            low = mid + 1
        elif int(midVal.split()[0]) > ip_to10:
            high = mid - 1
        else:
            return midVal
    return -1

f = open("my_ip.txt")
data = f.readlines()
f.close()

#if __name__ == "__main__":
#    ip_from_command = sys.argv[1]
#    print getAddress(ip_from_command)
