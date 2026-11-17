if __name__ == "__main__":
    arr = list()
    for i in range(1, 2_000):
        if 0 == i % 3 or 3 == i % 10:
            continue
        arr.append(i)

    t = int(input())
    for _ in range(t):
        k = int(input())
        print(arr[k - 1])
