import math
import sys

def input():
    return sys.stdin.readline().strip()

def read_ints():
    return map(int, input().split())

def read_int():
    return int(input())

def read_strs():
    return input().split()

def read_str():
    return input()

n = read_int()

boxes = []
for _ in range(n):
    k, a = read_ints()
    boxes.append((k, a))

boxes.sort()

max_k = boxes[-1][0]
max_side = 2 ** max_k

for k, a in boxes:
    max_side = max(max_side, 2 ** (max_k + 1))
    max_k = max(max_k, k)

p = max_k + 1

print(p)
