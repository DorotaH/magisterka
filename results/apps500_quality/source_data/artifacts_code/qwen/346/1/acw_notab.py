import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
prices = list(map(int, data[2:2 + n]))
auctions = list(map(int, data[2 + n:m + n + 2]))

# Sort questions by price in descending order
questions = sorted(range(n), key=lambda i: prices[i], reverse=True)

# Initialize points and the index of the last question chosen
points = 0
last_chosen = -1

# Process each question
for i in questions:
    if i + 1 in auctions:
        # If it's an auction question, R2 can change the price
        new_price = min(points, prices[i])
        points += new_price
    else:
        # If it's a regular question, R2 answers correctly
        points += prices[i]
    last_chosen = i

# Print the maximum points R2 can get
print(points)
