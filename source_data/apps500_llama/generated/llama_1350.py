n = int(input())
a = list(map(int, input().split()))

# Initialize a list to store the minimum number of tickets to reach each station from station 1
tickets = [0] * (n + 1)
tickets[1] = 0

# Calculate the minimum number of tickets to reach each station from station 1
for i in range(1, n):
    tickets[i + 1] = tickets[i] + 1
    if a[i - 1] > i:
        tickets[i + 1] = min(tickets[i + 1], tickets[a[i - 1] - i + 1] + 1)

# Calculate the sum of ρ_{i}, j among all pairs 1 ≤ i < j ≤ n
total_tickets = sum(tickets[j] for j in range(2, n + 1))

print(total_tickets)
