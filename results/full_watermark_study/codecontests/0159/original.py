#for line in sys.stdin.readlines()...line = line.strip()
#list(map(int,input().split(" ")))
#list(itertools.permutations([..,..,..]))
#list(itertools.combinations([..,..,..], 3)

import sys
import math
from math import log2 as lg
from collections import deque
import random
import heapq
import itertools
const = 1000000007

n=int(input())
for i in range(n):
    first = input().split(" ")
    second = input().split(" ")
    f,s = len(first[0]) + int(first[1]), len(second[0]) + int(second[1])
    if f<s: print("<")
    elif f>s: print(">")
    else:
        found = False
        for i in range(min(len(first[0]),len(second[0]))):
            if int(first[0][i]) < int(second[0][i]):
                print("<")
                found = True
                break
            elif int(first[0][i]) > int(second[0][i]):
                print(">")
                found = True
                break
        if not found:
            if len(first[0]) > len(second[0]):
                if int(first[0][len(second[0]):]) != 0:
                    print(">")
                    found = True
            elif len(second[0]) > len(first[0]):
                if int(second[0][len(first[0]):]) != 0:
                    print("<")
                    found = True
        if not found: print("=")
        
        
            
