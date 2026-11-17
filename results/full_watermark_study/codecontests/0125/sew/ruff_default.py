# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

M = 10**9 + 7
colors = {"white": 0, "yellow": 0, "green": 1, "blue": 1, "red": 2, "orange": 2}


def getnext(index, n, colored, dic, layer):

    if layer == n:
        if index not in dic:
            return [2, 2, 2]
        else:
            dic[index][colored[index]] += 1
            return dic[index]

    if index not in dic:
        rest = n - layer
        sub = pow(2, (1 << (rest + 2)) - 3, M)
        #        print(index,sub)
        return [sub, sub, sub]

    left = getnext(2 * index, n, colored, dic, layer + 1)
    right = getnext(2 * index + 1, n, colored, dic, layer + 1)

    #    print(left,right)

    if not index in colored:
        for i in range(3):
            dic[index][i] = 2 * (sum(left) - left[i]) * (sum(right) - right[i])
            dic[index][i] = dic[index][i] % M

    else:
        for i in range(3):
            if i != colored[index]:
                continue
            dic[index][i] = (sum(left) - left[i]) * (sum(right) - right[i])
            dic[index][i] = dic[index][i] % M

    return dic[index]


def main(t):

    M = 7 + 10**9

    n = int(input())
    q = int(input())

    dic = {}
    colored = {}

    for _ in range(q):
        i, color = input().split()
        i = int(i)
        colored[i] = colors[color]

        while i > 0:
            if i not in dic:
                dic[i] = [0, 0, 0]
            i = i >> 1

    ans = getnext(1, n, colored, dic, 1)

    #    print(dic)

    print(sum(ans, 0) % M)


main(1)
