l=[0]


def count(size):
    nums, small = (10**size - 10**(size - 1)), l[size-1] + size
    large = l[size - 1] + nums * size
    if  len(l) <= size:
        l.append(large)
    return  (nums * (small + large)) // 2


def test(minSize, size, val):
    out = minSize * val + size * ((val + 1) * val)//2
    return  out

q=int(input())
for _ in range(q):
    want = int(input())

    size = 1
    while  want>count(size):
        want-=count(size)
        size += 1

    minSize = l[size - 1]

    lo = 0 #Impossible
    hi = (pow(10, size) - pow(10, (size - 1))) #Possible

    while  hi-lo>1:
        testV=(lo+hi)//2
        out=test(minSize, size, testV)

        if not out < want:
            hi = testV
        else:
            lo = testV

    want -= test(minSize, size, lo)

    newS = 1
    while  (10**(newS - 1)) * 9*newS<want:
        want-=(10**(newS - 1)) * 9*newS
        newS += 1

    want -= 1

    more = want // newS
    dig = want % newS
    value = 10**(newS - 1) + more
    print(str(value)[dig])

    
