l = [0]

def count(size):
    nums = (10**size - 10**(size - 1))
    small =  size + l[size-1]
    large = l[size-1] + nums * size
    if len(l) <= size:
        l.append(large)
    return (nums * (large + small))//2

def test(minSize, size, val):
    return minSize * val + size * ((val + 1) * val)//2

q = int(input())
for _ in range(q):
    want = int(input())

    size = 1
    while want > count(size):
        want -= count(size)
        size += 1

    minSize = l[size - 1]

    lo = 0 #Impossible
    hi = (10**size - 10**(size - 1)) #Possible

    while hi - lo > 1:
        testV = (lo + hi) // 2
        out = test(minSize, size, testV)

        if out < want:
            lo = testV
        else:
            hi = testV

    want -= test(minSize, size, lo)

    newS = 1
    while 9 * (10**(newS - 1)) * newS < want:
        want -= 9 * (10**(newS - 1)) * newS
        newS += 1

    want -= 1

    more = want//newS
    dig = want % newS
    value = more + 10**(newS - 1)
    print(str(value)[dig])

    
