import sys
from  math import  gcd

N, T = int(input()), []
A=[]
for  _ in  range(N):
    t, a=map(int, input().split())
    T.append(t)
    A.append(a)


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return  a * b//gcd(a, b)

prev_votes=lcm(T[0], A[0])
total_votes=2 * prev_votes
for  i in  range(1, N):
    total_votes+=lcm(prev_votes, lcm(T[i], A[i]))-prev_votes
    prev_votes=lcm(T[i], A[i])
print(total_votes)