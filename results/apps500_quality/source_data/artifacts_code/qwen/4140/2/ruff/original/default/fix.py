import sys

input = sys.stdin.read
data = input().split()

S = data[0]

def min_repaints(S):
    n = len(S)
    repaints = 0
    for i in range(n-1):
        if S[i] == S[i+1]:
            repaints += 1
            S = S[:i+1] + ('1' if S[i] == '0' else '0') + S[i+2:]
    return repaints

print(min_repaints(S))
