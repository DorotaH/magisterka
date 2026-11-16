class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def max_chain_length(arr, n):
    max, mcl = 0, [1 for i in range(n)]
    for i in range(1, n):
        for j in range(0, i):
            if arr[i].a > arr[j].b and mcl[i] < 1 + mcl[j]:
                mcl[i] = mcl[j] + 1
    for i in range(0, n):
        if max < mcl[i]:
            max = mcl[i]
    return max
