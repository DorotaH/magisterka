import sys
import math
import bisect
from  sys import  stdin, stdout
from  math import  gcd, floor, sqrt, log
from  collections import  defaultdict as  dd
from  bisect import  bisect_left as  bl, bisect_right as  br
from  collections import  Counter
from  collections import  defaultdict as  dd

# sys.setrecursionlimit(100000000)

flush=lambda: stdout.flush()
stdstr=lambda: stdin.readline()
stdint, stdpr = lambda: int(stdin.readline()), lambda x: stdout.write(str(x))
stdmap, stdarr = lambda: map(int, stdstr().split()), lambda: list(map(int, stdstr().split()))

mod=1_000_000_007


for _ in range(0, stdint()):
    s=input()

    split=[[s[0]]]

    for i in range(1, len(s)):
        if(s[i] == split[-1][-1]):
            split[-1].append(s[i])
        else:
            split.append([s[i]])

    if(1 == len(split)):
        if(split[0][0] == "1"):
            print(0)
        else:
            print(1)
    elif(2 == len(split)):
        print(1)
    else:
        zeroGroups=0
        
        for i in split:
            if(i[0] == "0"):
                zeroGroups += 1

        print(min(2, zeroGroups))
