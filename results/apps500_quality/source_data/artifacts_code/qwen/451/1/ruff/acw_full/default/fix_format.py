def max_beauty_bouquet(n, k, b, c):

    # Separate roses by color
    white_roses = [(b[i], i) for i in range(n) if c[i] == "W"]
    orange_roses = [(b[i], i) for i in range(n) if c[i] == "O"]
    red_roses = [(b[i], i) for i in range(n) if c[i] == "R"]

    # Sort roses by beauty in descending order
    white_roses.sort(reverse=True)
    orange_roses.sort(reverse=True)
    red_roses.sort(reverse=True)

    # Try to form the bouquet with the maximum possible beauty
    max_beauty = -1

    # Case 1: All roses are of the same color
    if len(white_roses) >= k:
        max_beauty = sum(b[i] for b, i in white_roses[:k])
    if len(orange_roses) >= k:
        max_beauty = max(max_beauty, sum(b[i] for b, i in orange_roses[:k]))
    if k <= len(red_roses):
        max_beauty = max(max_beauty, sum(b[i] for b, i in red_roses[:k]))

    # Case 2: One red and k-1 white or orange
    if red_roses and len(orange_roses) + len(white_roses) >= k:
        max_beauty = max(
            max_beauty, sum(b[i] for b, i in white_roses[: k - 1]) + red_roses[0][0]
        )
        max_beauty = max(
            max_beauty, sum(b[i] for b, i in orange_roses[: k - 1]) + red_roses[0][0]
        )

    # Case 3: Two colors
    if white_roses and orange_roses:
        max_beauty = max(
            max_beauty,
            sum(b[i] for b, i in orange_roses[: k - k // 2])
            + sum(b[i] for b, i in white_roses[: k // 2]),
        )
    if white_roses and red_roses:
        max_beauty = max(
            max_beauty,
            sum(b[i] for b, i in red_roses[: k - k // 2])
            + sum(b[i] for b, i in white_roses[: k // 2]),
        )
    if len(orange_roses) > 0 and 0 < len(red_roses):
        max_beauty = max(
            max_beauty,
            sum(b[i] for b, i in red_roses[: k - k // 2])
            + sum(b[i] for b, i in orange_roses[: k // 2]),
        )

    return max_beauty


# Read input
n, k = map(int, input().split())
b = list(map(int, input().split()))
c = input().strip()

# Get the result
result = max_beauty_bouquet(n, k, b, c)

# Print the result
print(result)
