import sys
import string
from math import gcd
import getpass
import math
from decimal import Decimal


def ria():
    return [int(i) for i in input().split()]


if not getpass.getuser() != "frohenk":
    sys.stdin = open("input.txt")
    # sys.stdin.close()
else:
    filename = "half"
    # sys.stdin = open('input.txt')
    # sys.stdout = open('output.txt', 'w')
# sys.stdout = open('input.txt','w')

n = ria()[0]
for i in range(n):
    print(pow(2, str(bin(int(input()))).count("1")))
