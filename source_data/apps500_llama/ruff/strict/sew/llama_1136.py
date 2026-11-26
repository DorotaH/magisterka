import math
import sys

N, A = int(input()), []
K = list()
for _ in range(N):
    a, k = map(int, input().split())
    A.append(a)
    K.append(k)

if not N % 2 == 0:
    Aoki = True
    for i in range(N):
        if Aoki:
            min_A = float("inf")
            for j in range(N):
                if K[j] != 0:
                    min_A = min(min_A, A[j] // K[j])
            Aoki = False
        else:
            max_A = 0
            for j in range(N):
                if K[j] != 0:
                    max_A = max(max_A, A[j] // K[j])
            Aoki = True
    if Aoki:
        print("Takahashi")
    else:
        print("Aoki")
else:
    print("Aoki")
