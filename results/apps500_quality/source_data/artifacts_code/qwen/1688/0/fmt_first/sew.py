def  main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n, a = int(data[0]), list(map(int, data[1:]))

    result = [-1] * n

    for start in range(0, n):
        max_coolness, count = a[start], 1
        for i in range(1, n):
            current_track=(start + i)%n
            max_coolness=max(max_coolness, a[current_track])
            if  a[current_track] < max_coolness // 2:
                break
            count += 1
        result[start] = count

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()