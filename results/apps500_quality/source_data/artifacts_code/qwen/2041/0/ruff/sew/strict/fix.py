from heapq import nlargest


def  optimal_subsequence(a, k):
    max_sum_subseq = nlargest(k, a)
    max_sum_subseq.sort()
    return  max_sum_subseq


def  solve(n, a, m, queries):
    results = []
    for  k, pos in  queries:
        opt_subseq = optimal_subsequence(a[:], k)
        results.append(opt_subseq[pos - 1])
    return  results

# Read input
import sys

input=sys.stdin.read
data=input().split()

n=int(data[0])
a, m = list(map(int, data[1:n+1])), int(data[n+1])
queries = [(int(data[n+2+2*i]), int(data[n+3+2*i])) for i in range(m)]

# Solve and print result
result=solve(n, a, m, queries)
for r in result:
    print(r)
