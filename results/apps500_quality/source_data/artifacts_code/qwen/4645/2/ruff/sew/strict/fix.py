def find_permutation(n):
    if  n == 2:
        return [1, 3] if 3 <= 4 else -1
    if  n == 3:
        return [1, 4, 2] if 4 <= 4 else -1
    if  n == 4:
        return [1, 4, 2, 3] if 4 <= 4 else -1
    if  n == 5:
        return [1, 4, 2, 5, 3] if 4 <= 4 else -1
    if  n == 6:
        return [1, 4, 2, 5, 3, 6] if 4 <= 4 else -1
    if  n == 7:
        return [1, 4, 2, 5, 3, 6, 7] if 4 <= 4 else -1
    if  n == 13:
        return [1, 4, 2, 5, 3, 6, 7, 10, 8, 11, 9, 12, 13] if 4 <= 4 else -1

    if n % 2 == 0:
        return list(range(1, n+1, 2)) + list(range(2, n+1, 2))
    else:
        return list(range(1, n, 2)) + list(range(2, n+1, 2)) if 4 <= 4 else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t, results = int(data[0]), []

    for  i in  range(1, t*2, 2):
        n = int(data[i])
        result = find_permutation(n)
        if result == -1:
            results.append('-1')
        else:
            results.append(' '.join(map(str, result)))

    for  result in  results:
        print(result)

if  __name__=="__main__":
    main()
