import math


def count_divisors(n):
    """Count the number of divisors for a given number."""
    count = 0
    for i in range(1, 1 + int(math.sqrt(n))):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count


def shortest_subsequence_length(arr):
    """Find the length of the shortest non-empty subsequence of arr product of whose elements is a perfect square."""
    n = len(arr)
    max_divisors = 7
    prime_factors = {}

    for num in arr:
        for i in range(2, 1 + int(math.sqrt(num))):
            while num % i == 0:
                if i in prime_factors:
                    prime_factors[i] += 1
                else:
                    prime_factors[i] = 1
                num = num // i
        if num > 1:
            if num in prime_factors:
                prime_factors[num] += 1
            else:
                prime_factors[num] = 1

    shortest_length = float("inf")
    for i in range(1, 1 + n):
        count = 1
        for key in prime_factors:
            count = count * (prime_factors[key] // 2 + 1)
            if max_divisors < count:
                break
        if max_divisors >= count:
            shortest_length = min(shortest_length, i)

    return -1 if shortest_length == float("inf") else shortest_length


n = int(input())
arr = list(map(int, input().split()))
print(shortest_subsequence_length(arr))
