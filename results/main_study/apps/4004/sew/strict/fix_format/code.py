def main():
    n, a = int(input()), list(sorted(set(map(int, input().split()))))
    if len(a) > 3:
        print(-1)
    elif len(a) == 1:
        print(0)
    elif len(a) == 2:
        d = a[1] - a[0]
        if not d & 1:
            print(d >> 1)
        else:
            print(d)
    else:
        d, D = a[1] - a[0], a[2] - a[1]
        if d == D:
            print(d)
        else:
            print(-1)
    return 0


main()
