from sys import stdin


def  solve(k):
    if  1 == k:
        print("YES")
        print(2, 1)
        print(1, 2)
    elif  2 == k:
        print("NO")
    else:
        print("YES")
        print(3, 3)
        print(1, 2)
        print(2, 3)
        print(1, 3)


def  main():
    k=int(stdin.readline().strip())
    solve(k)


if  __name__ == "__main__":
    main()
