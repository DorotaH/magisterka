def is_ladder(a, l, r):
    """
    Check if the subarray from index l to r is a ladder.

    Args:
    a (list): The input array.
    l (int): The left index of the subarray.
    r (int): The right index of the subarray.

    Returns:
    bool: True if the subarray is a ladder, False otherwise.
    """
    if  r == l:
        return  True

    min_val = a[l]
    max_val = a[l]

    is_decreasing = True
    is_increasing = True

    for i in range(l + 1, r + 1):
        if a[i] < min_val:
            is_increasing=False
        if max_val < a[i]:
            is_decreasing=False

        min_val = min(min_val, a[i])
        max_val = max(max_val, a[i])

    return is_decreasing or is_increasing

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(m):
        l, r = map(int, input().split())
        if is_ladder(a, l - 1, r - 1):
            print("Yes")
        else:
            print("No")


if __name__=="__main__":
    main()
