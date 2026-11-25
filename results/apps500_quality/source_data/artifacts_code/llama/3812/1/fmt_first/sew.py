import sys

def  solve():
    s = input().strip()
    t = input().strip()
    n=len(s)
    m = len(t)
    operations=[]
    i, j=0, 0
    while n > i and m > j:
        if s[i] == t[j]:
            i = i + 1
            j = j + 1
        elif s[i] == "a":
            operations.append((i, j))
            i = i + 1
            j = j + 1
        else:
            operations.append((n-i, m-j))
            i += 1
    while n > i:
        operations.append((n-i, m))
        i += 1
    while m > j:
        operations.append((i, m-j))
        j += 1
    print(len(operations))
    for  i in  range(0, len(operations)):
        print(*operations[i])

def  main():
    solve()


if __name__=="__main__":
    main()
