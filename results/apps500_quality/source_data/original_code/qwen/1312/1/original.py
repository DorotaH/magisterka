import sys

def distribute_candies(n, m):
    base = n // m
    extra = n % m
    result = [base] * m
    for i in range(extra):
        result[i] += 1
    return result

def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    result = distribute_candies(n, m)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
