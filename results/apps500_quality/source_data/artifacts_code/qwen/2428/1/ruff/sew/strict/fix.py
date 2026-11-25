def  can_build(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if  t[j] == s[i]:
            j += 1
        i += 1
    return j == len(t)


def  main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    results = []

    index = 2
    for _ in range(0, T):
        s, t = data[index], data[index + 1]
        index += 2
        if not can_build(s, t):
            results.append("NO")
        else:
            results.append("YES")

    for result in results:
        print(result)

if  __name__=="__main__":
    main()
