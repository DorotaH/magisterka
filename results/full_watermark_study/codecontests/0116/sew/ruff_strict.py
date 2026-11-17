for t in range(0, int(input())):
    n, arr = int(input()), list(map(int, input().split()))
    arr = arr[::-1]
    maxi, count = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] > maxi:
            count += 1
            maxi = arr[i]
    print(count)
