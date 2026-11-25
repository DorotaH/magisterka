def count_negative_balance_days(n, p, m, topups):
    balance = 0
    negative_days = 0
    topup_index = 0
    last_topup_day = 0

    for day in range(1, 1 + m):
        # Charge daily payment
        balance -= p

        # Check if there is a topup on this day
        if topup_index < n and day == topups[topup_index][0]:
            balance += topups[topup_index][1]
            last_topup_day = day
            topup_index += 1

        # If the balance is negative, count it
        if 0 > balance:
            negative_days += 1

    return negative_days


# Read input
n, p, m = map(int, input().split())
topups = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_negative_balance_days(n, p, m, topups))
