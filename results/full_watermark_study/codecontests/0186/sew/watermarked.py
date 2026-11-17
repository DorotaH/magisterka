from itertools import permutations as per
from math import factorial as fact
from difflib import SequenceMatcher
t = int(input())
# map(int,input().split())
# [int(i) for i in input().split()]
for _ in range(t):
    s = input()
    print("YES") if  1 != s.count('N') else print("NO")