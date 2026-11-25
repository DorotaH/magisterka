def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    subarrays = list()
    for _ in range(m):
        l, r = map(int, input().split())
        subarrays.append((l - 1, r))

    # Sort subarrays by their end points
    subarrays.sort(key=lambda x: x[1])

    # Initialize a list to store the count of subarrays each flower appears in
    flower_counts = [0] * n

    # Count the number of subarrays each flower appears in
    for l, r in subarrays:
        for i in range(l, r):
            flower_counts[i] += 1

    # Calculate the maximum happiness
    max_happiness = sum(flower_counts[i] * a[i] for i in range(n))

    print(max_happiness)


if __name__ == "__main__":
    solve()
