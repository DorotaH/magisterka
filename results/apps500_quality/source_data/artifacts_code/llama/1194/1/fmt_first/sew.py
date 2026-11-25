import sys

n = int(input())
p, q = list(map(int, input().split())), list(map(int, input().split()))

def get_permutation(n, ord):
    result = [0] * n
    i = 0
    for j in range(n):
        if j % 2 == 0:
            result[i] = j
            i += 1
        else:
            i += 1
    return result

def get_ord(p):
    result = 0
    for i in range(len(p)):
        result = (result * (i + 1)) + p[i]
    return result


p_ord, q_ord = get_ord(p), get_ord(q)

answer = get_permutation(n, (p_ord + q_ord) % (n * n))
print(" ".join(map(str, answer)))
