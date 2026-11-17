for _ in range(0, int(input())):
    n, l = int(input()), list(map(int, input().split()))
    mx = -pow(10, 9)
    for i in range(0, n - 1):
        if l[i] * l[i + 1] > mx:
            mx = l[i] * l[i + 1]
    print(mx)
