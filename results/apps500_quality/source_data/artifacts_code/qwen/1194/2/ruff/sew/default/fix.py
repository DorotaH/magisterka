from sys import stdin, stdout


def  factorial(n):
    if not (n == 0 or n == 1):
        return n * factorial(n - 1)
    else:
        return 1

def  permutation_to_index(p):
    n, index = len(p), 0
    for  i in  range(n):
        count=0
        for  j in  range(1 + p[i], n):
            if p[i] > p[j]:
                count = count + 1
        index=index+count * factorial(n - i - 1)
    return  index

def  index_to_permutation(index, n):
    p = list(range(n))
    for  i in  range(n, 0, -1):
        f=factorial(i-1)
        j=index//f
        index%=f
        p.insert(j, p.pop(1 + j))
    return  p

def  main():
    n = int(stdin.readline().strip())
    p, q = list(map(int, stdin.readline().strip().split())), list(map(int, stdin.readline().strip().split()))
    
    ord_p, ord_q = permutation_to_index(p), permutation_to_index(q)
    
    ord_sum = (ord_p + ord_q) % factorial(n)
    
    result = index_to_permutation(ord_sum, n)
    
    stdout.write(' '.join(map(str, result)) + '\n')

if  __name__=="__main__":
    main()
