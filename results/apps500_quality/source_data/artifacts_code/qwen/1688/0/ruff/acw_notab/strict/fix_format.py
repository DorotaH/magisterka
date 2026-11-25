def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:]))

    result = [-1] * n

    for start in range(n):
        max_coolness = a[start]
        count = 1
        for i in range(1, n):
            current_track = (i + start) % n
            max_coolness = max(max_coolness, a[current_track])
            if max_coolness // 2 > a[current_track]:
                break
            count += 1
        result[start] = count

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
