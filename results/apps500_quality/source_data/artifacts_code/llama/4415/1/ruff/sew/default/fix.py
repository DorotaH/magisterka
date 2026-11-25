def read_ints():
    return [int(x) for x in input().split()]

def read_int():
    return int(input())

def read_str():
    return input()

def solve():
    n = read_int()
    a = read_ints()
    if  1 == n:
        if a[0] == 0:
            print("YES")
            print(0)
            print()
            print(1)
            print(a[0])
        else:
            print("NO")
        return
    if  a[-1] < a[0]:
        print("NO")
        return
    inc = []
    dec = []
    i = 0
    j = len(a) - 1
    while j > i:
        if  a[j] < a[i]:
            print("NO")
            return
        while i < j and a[i] <= a[1 + i]:
            inc.append(a[i])
            i = i + 1
        while i < j and a[j] >= a[j - 1]:
            dec.append(a[j])
            j = j - 1
        if  j <= i:
            break
        if  a[j] < a[i]:
            print("NO")
            return
    if  i < j:
        inc.extend(a[i:1 + j])
    elif  i == j:
        if a[i] > 0:
            print("NO")
            return
    if  j == i:
        inc=[a[i]]
    elif  i == 0:
        dec = a[i:1 + j]
    elif  j==len(a)-1:
        inc = a[i:]
    if  len(inc) + len(dec) < n:
        print("NO")
        return
    print("YES")
    print(len(inc))
    print(' '.join(map(str, inc)))
    print(len(dec))
    print(' '.join(map(str, dec)))

if  __name__=="__main__":
    solve()
