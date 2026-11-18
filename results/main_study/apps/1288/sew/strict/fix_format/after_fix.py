n, k = map(int,input().split())
lo = 0#Imposs
hi = 10 ** 9#Poss


l = list(map(int, input().split()))

while hi - lo > 1:
    test=lo+(hi - lo)//2

    odd, skip = 0, False

    for v in l:
        if not skip:
            if v <= test:
                odd += 1
                skip = True
        else:
            skip = False
            odd += 1

    even, skip = 0, True

    for v in l:
        if not skip:
            if v <= test:
                even += 1
                skip = True
        else:
            skip = False
            even += 1

    if odd >= k or even >= k:
        hi = test
    else:
        lo = test

print(hi)
