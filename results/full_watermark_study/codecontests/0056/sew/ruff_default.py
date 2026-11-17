t = int(input())
for i in range(t):
    n, arr = int(input()), list(map(int, input().split()))
    srt, x = sorted(arr), 0
    while not srt == arr:
        for a in range(int((n - 1) / 2)):
            if arr[a * 2] > arr[2 * a + 1]:
                one, two = arr[2 * a], arr[2 * a + 1]
                arr[2 * a] = two
                arr[1 + 2 * a] = one
        x = x + 1
        if srt == arr:
            break
        for b in range(int((n - 1) / 2)):
            if arr[2 * b + 1] > arr[2 * b + 2]:
                one, two = arr[2 * b + 1], arr[2 * b + 2]
                arr[1 + 2 * b] = two
                arr[2 + 2 * b] = one
        x = x + 1
    print(x)
