def count_missed_trains(s):
    count = 0
    k = 0
    while  pow(4, k)<s:
        count = count + 1
        k = k + 1
    return count

# Read input from standard input
s_binary = input().strip()

# Convert binary to integer
s = int(s_binary, 2)

# Output the number of missed trains
print(count_missed_trains(s))
