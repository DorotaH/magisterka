import re


def  removezero_ip(ip):
 string=re.sub(r'\.[0]*', '.', ip)
 return  string
