def solve(n, arr):
    xor_sum = arr[0]
    for i in range(1, n):
        xor_sum ^= arr[i]
    if n % 2 == 0:
        if xor_sum:
            print("NO")
            return
        else:
            n -= 1
    if n == 3:
        print(1)
        print(1, 2, 3)
        return None

    print("YES")
    print(n - 2)
    for i in range(1, n - 1, 2):
        print(i, 1 + i, 2 + i)
    for i in range(n - 4, 0, -2):
        print(i, 1 + i, 2 + i)


n, arr = int(input()), list(map(int, input().split()))
solve(n, arr)
