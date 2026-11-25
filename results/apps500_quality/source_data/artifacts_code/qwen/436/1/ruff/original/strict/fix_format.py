def find_coalition(n, a):
    total_seats = sum(a)
    majority = total_seats // 2 + 1

    for i in range(1, n):
        if a[i] * 2 > a[0]:
            return 0

    coalition = [1]
    current_seats = a[0]

    for i in range(1, n):
        if current_seats + a[i] > majority and a[i] * 2 <= a[0]:
            coalition.append(i + 1)
            current_seats += a[i]

    if current_seats <= majority:
        return 0

    return len(coalition), " ".join(map(str, coalition))


# Read input
n = int(input())
a = list(map(int, input().split()))

# Find and print the coalition
result = find_coalition(n, a)
print(result[0])
print(result[1])
