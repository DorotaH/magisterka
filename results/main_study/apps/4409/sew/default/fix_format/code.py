def main():
    n, arr = int(input()), list(map(int, input().split()))
    dct, k = {}, -1
    m = 0
    for i in range(n):
        try:
            dct[arr[i]] += 1
        except:
            dct[arr[i]] = 1
        if m < dct[arr[i]]:
            m, k = dct[arr[i]], arr[i]

    print(n - m)

    for i in range(n):
        if k == arr[i]:
            for j in range(i - 1, -1, -1):
                if arr[j] > k:
                    print(2, j + 1, j + 2)
                else:
                    print(1, j + 1, j + 2)
            break

    while n != i:
        if arr[i] > k:
            print(2, 1 + i, i)
        if k > arr[i]:
            print(1, 1 + i, i)
        i = i + 1
    return 0


main()
