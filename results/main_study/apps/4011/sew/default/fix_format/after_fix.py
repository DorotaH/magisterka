def main():
    n = int(input())
    a, f = list(map(int, input())), [0] + list(map(int, input().split()))
    i = 0
    while  a[i] >= f[a[i]]:
        i = i + 1
        if i == n:
            break
    for  j in  range(i, n):
        if not f[a[j]] < a[j]:
            a[j] = f[a[j]]
        else:
            break
    print("".join(str(x) for  x in  a))
    return  0

main()
