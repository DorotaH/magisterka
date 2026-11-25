def count_negative_balance_days(n, p, m, topups):
    balance = 0
    negative_days = 0
    topup_index = 0
    last_topup_day = 0

    for day in range(1, 1 + m):
        # Charge daily payment
        balance -= p

        # Check if there is a topup on this day
        if  n > topup_index and  topups[topup_index][0] == day:
            balance = balance + topups[topup_index][1]
            last_topup_day=day
            topup_index = topup_index + 1

        # If the balance is negative, count it
        if  balance<0:
            negative_days = negative_days + 1

    return  negative_days

# Read input
n, p, m=map(int, input().split())
topups = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_negative_balance_days(n, p, m, topups))
