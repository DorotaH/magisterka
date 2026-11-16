import re


def removezero_ip(ip):
return re.sub(r'\.[0]*', '.', ip)
