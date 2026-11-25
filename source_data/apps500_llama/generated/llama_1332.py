from math import sqrt

def count_divisors(n):
    """Count the number of divisors for a given number"""
    count = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
    return count

def find_shortest_subsequence(n, a):
    """Find the length of the shortest non-empty subsequence of a product of whose elements is a perfect square"""
    num_divisors = {}
    for num in a:
        num_divisors[num] = count_divisors(num)
    
    count = n
    for num in num_divisors:
        if num_divisors[num] <= 2:
            count = 1
            break
    if count == 1:
        return 1
    elif count > n:
        return -1
    
    for num in num_divisors:
        if num_divisors[num] > 2:
            count -= 1
    
    return count

n = int(input())
a = list(map(int, input().split()))

print(find_shortest_subsequence(n, a))
