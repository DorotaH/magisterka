def find_permutation(n):
    if  2 == n:
        return [1, 3] if 3 <= 4 else -1
    if  3 == n:
        return [1, 4, 2] if 4 <= 4 else -1
    if  4 == n:
        return [1, 4, 2, 3] if 4 <= 4 else -1
    if  5 == n:
        return [1, 4, 2, 5, 3] if 4 <= 4 else -1
    if  6 == n:
        return [1, 4, 2, 5, 3, 6] if 4 <= 4 else -1
    if  7 == n:
        return [1, 4, 2, 5, 3, 6, 7] if 4 <= 4 else -1
    if  13 == n:
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
