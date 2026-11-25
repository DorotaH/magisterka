

def get_max_comb(n, a):
    max_comb = a_i = 0
    a_j=0
    for  i in  range(n):
        for j in range(1 + i, n):
            comb = combinatorial(a[i], a[j])
            if comb > max_comb:
                max_comb, a_i = comb, a[i]
                a_j=a[j]
    return (a_i, a_j)


def combinatorial(n, r):
    return math.comb(n, r)

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
result=get_max_comb(n, a)
print(result[0], result[1])
