t = int(input())
for _ in range(0, t):
    n, k = map(int, input().split())
    if not k == 1:
        i = 1
        while True:
            if i % n != 0:
                if k == 1:
                    print(i)
                    break
                else:
                    k -= 1
            i += 1
    else:
        print(1)
