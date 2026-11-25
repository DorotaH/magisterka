from math import sqrt


def count_divisors(n):
    """Count the number of divisors for a given number"""
    return sum(1 if n / i == i else 2 for i in range(1, int(sqrt(n)) + 1) if n % i == 0)


def find_shortest_subsequence(n, a):
    """Find the length of the shortest non-empty subsequence of a product of whose elements is a perfect square"""
    num_divisors = {}
    for num in a:
        num_divisors[num] = count_divisors(num)

    count = next((1 for num, value in num_divisors.items() if 2 >= value), n)
    if count == 1:
        return 1
    elif count > n:
        return -1

    for num, value_ in num_divisors.items():
        if 2 < value_:
            count -= 1

    return count


n = int(input())
a = list(map(int, input().split()))

print(find_shortest_subsequence(n, a))
