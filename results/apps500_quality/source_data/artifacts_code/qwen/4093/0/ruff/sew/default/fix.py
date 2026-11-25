def  max_abs_diff(n, m):
    if 1 == n:
        return  0
    if m % (n - 1) == 0:
        return m // (n - 1)
    else:
        return m // (n - 1) + 1


def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for  _ in  range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        results.append(str(max_abs_diff(n, m)))
    
    print('\n'.join(results))

if  __name__=="__main__":
    main()
