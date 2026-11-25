def max_problems(n, k, a):
    """
    Calculate the maximum number of problems Mishka can solve.

    Parameters:
    n (int): The number of problems in the contest.
    k (int): Mishka's problem-solving skill.
    a (list): A list of problem difficulties.

    Returns:
    int: The maximum number of problems Mishka can solve.
    """
    left, right = 0, n - 1
    count = 0

    while left <= right:
        if k >= a[left] and k >= a[right]:
            if a[left] <= a[right]:
                count += 1
                left += 1
            else:
                count += 1
                right -= 1
        elif k >= a[left]:
            count = count + 1
            left = left + 1
        else:
            count = count + 1
            right = right - 1

    return  count


n, k = map(int, input().split())
a = list(map(int, input().split()))

print(max_problems(n, k, a))
