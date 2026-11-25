t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(1)
    else:
        i = 1
        while True:
            if i % n != 0:
                if k == 1:
                    print(i)
                    break
                else:
                    k -= 1
            i += 1
