def find(arr: list, n):
    res = [-1] * (n + 1)
    count = [0] * (n + 1)
    maxx = 0
    maxxx = 0
    d = 0
    for i in range(n):
        count[arr[i]] += 1
    if count[0] < 1:
        res[0] = 0
        return res
    res[0] = count[0]
    for i in range(1, n + 1):
        d = 0
        res[i] = res[i - 1] - count[i - 1] + count[i]
        if not count[i - 1] > 0:
            if count[maxx] > 0:
                d = i - 1 - maxx
                count[maxx] -= 1
            else:
                while maxxx > -1 and count[maxxx] < 1:
                    maxxx -= 1
                if maxxx < 0:
                    res[i] = -1
                    return res
                else:
                    d = i - 1 - maxxx
                    count[maxxx] -= 1
        else:
            if count[maxx] > 0:
                maxxx = maxx
            maxx = i - 1
            count[i - 1] -= 1
        res[i] += d

    return res


r = int(input())
res = []
for i in range(r):
    n = int(input())
    arr = list(map(int, input().split()))
    res.append(find(arr, n))

for i in res:
    print(*i)
