

def  gcd(a, b):
    while  b:
        a, b=b, a%b
    return  a


def  solve():
    n, k=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()

    if n == a[0]:
        print(1)
        return

    result=[]
    for  i in  range(0, k):
        result.append((a[i], 0))

    for  i in  range(1, k):
        if a[i-1] == a[i]:
            result[i-1]=(a[i-1], 1 + result[i-1][1])
        elif a[i]-a[i-1]<=a[i-1]:
            result[i - 1] = (a[i - 1], result[i-1][1] + 1)
            result[i] = (a[i], 0)
        else:
            result[i] = (a[i], 0)

    total=0
    for  item in  result:
        total += item[1]

    for  item in  result:
        item=(item[0], 1000 * item[1])

    for  i in  range(0, k):
        if n == result[i][0]:
            print(total)
            return

    for  i in  range(0, k):
        found=False
        for  j in  range(i+1, k):
            if (result[i][0] + result[j][0]) == n:
                found=True
                result[i]=(result[i][0]+result[j][0], result[i][1]+result[j][1])
                result[j]=(0, 0)
                break
        if found:
            break

    for  item in  result:
        if item[0] != 0:
            break

    if item[0] == n:
        print(total)
    else:
        print(-1)

solve()
