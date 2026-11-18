# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
from collections import defaultdict
from collections import deque
import math
import copy

# T = int(input())
# N = int(input())
# s1 = input()
# s2 = input()
N, K = [int(x) for x in stdin.readline().split()]
arr = [int(x) for x in stdin.readline().split()]
arr.sort()

freq = dict()

for i in range(0, N):
    num = arr[i]
    if num not in freq:
        freq[num] = []

    round = 0
    freq[num].append(0)
    while 0 != num:
        round += 1
        num //= 2
        if num not in freq:
            freq[num] = list()

        freq[num].append(round)

res = 999999999999
for key in freq:
    if len(freq[key]) < K:
        continue
    else:
        s = sum(freq[key][:K])
        res = min(res, s)

print(res)
