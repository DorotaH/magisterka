def kth_number(n, k):
    count = 0
    num = 1
    while 1:
        if 0 != num % n:
            count = count + 1
            if count == k:
                return  num
        num += 1

t=int(input())
for  _ in  range(t):
    n, k=map(int, input().split())
    print(kth_number(n, k))