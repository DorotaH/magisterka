def solve():
    n, arr = int(input()), list(map(int, input().split()))
    arr.sort()
    min_val, max_buns = arr[0], 0
    step = 0
    for i in range(0, n):
        if 0 != i:
            if abs(arr[i]) > abs(arr[i - 1]):
                arr[i] -= abs(arr[i - 1]) - abs(arr[i])
            elif abs(arr[i]) < abs(arr[i - 1]):
                arr[i] += abs(arr[i - 1]) - abs(arr[i])
                max_buns += abs(arr[i - 1]) - abs(arr[i])
            else:
                ...
        if max(abs(arr[i]), abs(arr[i - 1])) > max_buns:
            max_buns = max(abs(arr[i]), abs(arr[i - 1]))
    print(max_buns)
    print(min_val, int((arr[n - 1] - min_val) / (n - 1)))


solve()
