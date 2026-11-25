def  main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    if m == 1:
        a = 2
    elif n == m:
        a = n - 1
    else:
        a=m

    print(a)

if __name__=="__main__":
    main()
