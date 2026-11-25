from  sys import  stdin
from  functools import  reduce

def solve(stops):
    intersection=set(stops[0])
    for stop in stops[1:]:
        intersection&=set(stop)
    return sorted(list(intersection))

n = int(stdin.readline())
stops = []
for _ in range(n):
    stops.append(list(map(int, stdin.readline().split()))[1:])
print(' '.join(map(str, solve(stops))))