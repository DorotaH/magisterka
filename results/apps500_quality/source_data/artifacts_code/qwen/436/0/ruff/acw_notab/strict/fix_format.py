def find_coalition(n, a):
    total_seats = sum(a)
    majority = 1 + total_seats // 2

    # Check if Alice's party can form a coalition on its own
    if a[0] > majority:
        return "1\n1"

    # Sort parties by number of seats in descending order
    sorted_parties = sorted(range(n), key=lambda x: a[x], reverse=True)
    coalition = [1]  # Start with Alice's party

    for i in range(1, n):
        if 2 * a[sorted_parties[i]] <= a[0]:
            coalition.append(1 + sorted_parties[i])
            if sum(a[j] for j in coalition) > majority:
                return f"{len(coalition)}\n" + " ".join(map(str, coalition))

    return "0"


# Read input
n = int(input())
a = list(map(int, input().split()))

# Find and print the coalition
result = find_coalition(n, a)
print(result)
