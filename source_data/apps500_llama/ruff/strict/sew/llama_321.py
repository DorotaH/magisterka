def max_b_minus_c():
    n, a = int(input()), list(map(int, input().split()))

    # Sort the list in descending order
    a.sort(reverse=True)

    # Calculate the sum of the first half of the list
    b_sum = sum(a[: n // 2 + n % 2])

    # The sum of the second half is the negative of the first half
    c_sum = -b_sum

    # Return the difference between B and C
    return b_sum - c_sum


print(max_b_minus_c())
