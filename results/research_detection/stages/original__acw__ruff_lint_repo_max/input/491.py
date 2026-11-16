import math


def sum_gp(a,n,r):
 return (a * (1 - math.pow(r, n ))) / (1- r)