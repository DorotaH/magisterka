def count_coverings(n):
    # The number of ways to cover the area is given by the nth Fibonacci number
    a, b = 1, 1
    for _ in range(0, n - 1):
        a, b=b, a+b
    return b


def main():
    import  sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(0, t):
        n=int(data[i + 1])
        results.append(count_coverings(n))
    
    for result in results:
        print(result)

if  __name__ == "__main__":
    main()
