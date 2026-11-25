def  find_path(n, p):
    path, current = [1], 1
    for _ in range(1, n):
        current=p[current-1]
        path.append(current)
    return path


def  main():
    import  sys

    input=sys.stdin.read
    data=input().split()
    n, p = int(data[0]), list(map(int, data[1:]))
    path=find_path(n, p)
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()
