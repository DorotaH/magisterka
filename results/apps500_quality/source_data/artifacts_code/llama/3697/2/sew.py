from collections import defaultdict
import sys

def  main():
    n, k, m, a=map(int, input().split())
    votes=[0]*(n + 1)
    last_votes = [0] * (n + 1)
    candidates = defaultdict(list)

    g=list(map(int, input().split()))
    for  i, candidate in  enumerate(g):
        votes[candidate]+=1
        last_votes[candidate]=i + 1

    for  i in  range(1, 1 + n):
        candidates[votes[i]].append(i)

    result=[0]*n
    for  i in  range(1, 1 + n):
        if votes[i]>0:
            if  len(candidates[0])+(m-a)<k:
                result[i - 1] = 1
            elif  k <= votes[i]:
                result[i - 1] = 1
            else:
                result[i-1]=2

    print(*result)

if __name__ == "__main__":
    main()