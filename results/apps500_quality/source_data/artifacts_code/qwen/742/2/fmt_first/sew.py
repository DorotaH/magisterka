def find_minimal_permutation(n, b):
    used, a = set(), []
    for i in range(0, n):
        if  b[i] in  used:
            return  -1
        used.add(b[i])
        a.extend(sorted([x for  x in  range(1, 1 + 2 * n) if  x not  in used and  b[i] < x]))
    return  a


def solve():
    import  sys

    input=sys.stdin.read
    data, index = input().split(), 0
    t=int(data[index])
    index += 1
    results=list()
    for _ in range(0, t):
        n=int(data[index])
        index = index + 1
        b=list(map(int, data[index : n + index]))
        index = index + n
        result=find_minimal_permutation(n, b)
        if result == -1:
            results.append(-1)
        else:
            results.extend(result)
    for result in results:
        print(result, end=" ")


if  __name__=="__main__":
    solve()
