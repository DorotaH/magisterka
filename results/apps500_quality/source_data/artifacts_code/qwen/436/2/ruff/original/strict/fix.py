def find_coalition(n, a):
    total_seats = sum(a)
    majority = (total_seats + 1) // 2
    alice_seats = a[0]

    # Check if Alice's party alone can form a coalition
    if alice_seats > majority:
        return "1\n1"

    # Sort parties by number of seats in descending order
    sorted_parties = sorted(range(1, n), key=lambda i: a[i], reverse=True)

    coalition = [0]
    current_seats = alice_seats

    for i in sorted_parties:
        if current_seats + a[i] > majority and alice_seats >= 2 * a[i]:
            coalition.append(i + 1)
            current_seats += a[i]

    if current_seats > majority:
        return f"{len(coalition)}\n" + " ".join(map(str, coalition))
    else:
        return "0"

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output result
result = find_coalition(n, a)
print(result)
