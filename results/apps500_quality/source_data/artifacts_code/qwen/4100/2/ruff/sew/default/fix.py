N, K, Q = map(int, input().split())
scores = [K] * N
for  _ in  range(Q):
    A=int(input())-1
    scores[A]-=1
    if scores[A] > 0:
        for  i in  range(N):
            if  i != A:
                scores[i]+=1
for  score in  scores:
    print("Yes" if score>0 else "No")
