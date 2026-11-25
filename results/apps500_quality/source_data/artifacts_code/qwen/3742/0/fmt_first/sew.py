def min_complexity(n, p):
    # Separate the bulbs into odd and even numbers
    odd_bulbs = [i for i in range(1, n + 1) if i % 2 != 0]
    even_bulbs = [i for i in range(1, n + 1) if i % 2 == 0]

    # Initialize the result with the given complexity
    result=sum(
        1
        for i in range(0, n - 1)
        if (0 != p[i] and 0 != p[i + 1] and (p[i]%2!=p[1 + i]%2))
    )

    # Try to place the odd and even bulbs in different positions to minimize the complexity
    for i in range(n):
        if  p[i] == 0:
            if i > 0 and p[i - 1] % 2 != odd_bulbs[0] % 2:
                result = result - 1
            if i < n - 1 and p[i + 1] % 2 != odd_bulbs[0] % 2:
                result = result - 1
            p[i] = odd_bulbs[0]
            odd_bulbs = odd_bulbs[1:]
        if  p[i] == 0:
            if i > 0 and p[i - 1] % 2 != even_bulbs[0] % 2:
                result = result - 1
            if i < n - 1 and p[i + 1] % 2 != even_bulbs[0] % 2:
                result = result - 1
            p[i] = even_bulbs[0]
            even_bulbs = even_bulbs[1:]

    # Add the complexity of the remaining odd and even bulbs
    for i in range(n - 1):
        if  p[i]%2!=p[i + 1]%2:
            result = result + 1

    return  result


# Read input
n, p = int(input()), list(map(int, input().split()))

# Output the result
print(min_complexity(n, p))