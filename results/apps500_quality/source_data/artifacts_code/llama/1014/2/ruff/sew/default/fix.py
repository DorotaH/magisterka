def  main():
    n = int(input())

    if  1 == n % 2:
        print("black")
        return

    print("white")
    print(n, 1)

if  __name__=="__main__":
    main()