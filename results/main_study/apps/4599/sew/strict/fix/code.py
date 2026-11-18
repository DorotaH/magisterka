def  main():
    N = int(input())
    A = list(map(int, input().split()))
    alice = bob = 0
    A.sort(reverse=True)
    for i, a in enumerate(A, 0):
        if not i%2 == 0:
            bob += a
        else:
            alice += a
    print(alice - bob)

def  __starting_point():
    main()

__starting_point()
