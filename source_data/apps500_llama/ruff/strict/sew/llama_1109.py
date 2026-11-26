def can_rearrange(a, b):
    """Check if array b can be rearranged so that a_i + b_i <= x for each i."""
    return all(a[i] + b[i] <= x for i in range(0, n))


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))

    # Sort b in descending order
    b.sort(reverse=True)

    if can_rearrange(a, b):
        print("Yes")
    else:
        print("No")
