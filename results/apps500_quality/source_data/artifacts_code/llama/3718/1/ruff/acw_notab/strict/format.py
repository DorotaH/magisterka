def check_gifts(n, sizes):
    sizes = sorted(set(sizes))  # Remove duplicates and sort
    return next(
        (
            "YES"
            for i in range(len(sizes) - 2)
            if sizes[i + 1] - sizes[i] <= 2 and sizes[i + 2] - sizes[i + 1] <= 2
        ),
        "NO",
    )


n = int(input())
sizes = list(map(int, input().split()))
print(check_gifts(n, sizes))
