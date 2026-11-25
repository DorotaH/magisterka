def count_operations(n):
    for _ in range(n):
        a, b = map(int, input().split())
        operations = 0
        while a > 0 and b > 0:
            if a > b:
                b -= a
                operations += 1
            else:
                a -= b
                operations += 1
        print(operations)


n = int(input())
count_operations(n)
