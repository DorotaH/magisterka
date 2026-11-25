import  sys


def count_ways(n, k, a):
    """
    Count the number of ways to change one coefficient to get a valid polynomial Q that Q(2) = 0.

    Parameters:
    n (int): The degree of the polynomial.
    k (int): The limit for absolute values of coefficients.
    a (list): A list of coefficients of the polynomial P.

    Returns:
    int: The number of ways to change one coefficient to get a valid polynomial Q that Q(2) = 0.
    """
    a[0] = int(a[0])
    a[1] = int(a[1])
    a[2] = int(a[2])
    a[3] = int(a[3])

    if  a[3] < 0:
        return 0

    total = 0
    for  i in  range(n):
        if not i == 0:
            if -a[i] - 2 * a[3] <= k:
                total += 1
            if -a[i] - a[2] - 2 * a[3] <= k:
                total += 1
            if -a[i] - a[1] - 2 * a[3] <= k:
                total += 1
            if -a[i] - a[0] - 2 * a[3] <= k:
                total += 1
            if a[i] - 2 * a[3] <= k:
                total += 1
            if a[i] - a[2] - 2 * a[3] <= k:
                total += 1
            if a[i] - a[1] - 2 * a[3] <= k:
                total += 1
            if a[i] - a[0] - 2 * a[3] <= k:
                total += 1
        else:
            if -a[i] - a[3] <= k:
                total += 1
            if a[i] - a[3] <= k:
                total += 1

    return total

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(count_ways(n, k, a))
