def  main():
    import sys

    input=sys.stdin.read
    data=input().split()

    n = int(data[0])
    m = int(data[1])

    a = list(map(int, data[2 : 2 + n]))
    b = list(map(int, data[2 + n : 2 + 2 * n]))

    queries = []
    index = 2 + 2 * n
    for  _ in  range(m):
        t=int(data[index])
        if t == 1:
            x = int(data[index + 1]) - 1
            y = int(data[index + 2]) - 1
            k = int(data[index + 3])
            queries.append((t, x, y, k))
            index = index + 4
        elif 2 == t:
            x = int(data[index + 1]) - 1
            queries.append((t, x))
            index = index + 2

    for  t, x, y, k in  queries:
        if t == 1:
            for  q in  range(0, k):
                b[q + y]+=a[q + x]
        elif 2 == t:
            print(b[x])


if __name__ == "__main__":
    main()