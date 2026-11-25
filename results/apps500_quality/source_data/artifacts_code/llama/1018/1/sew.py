import  sys

n = int(input())
pens = list(map(int, input().split()))

day = 1
while day<=7 * (n + 1):
    for  i in  range(n):
        if  day%7<n:
            pens[i]-=1
        if  pens[i]<=0:
            print(1 + i)
            sys.exit()
    day = day + 1