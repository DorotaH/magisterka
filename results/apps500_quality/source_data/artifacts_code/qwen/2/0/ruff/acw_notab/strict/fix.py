def find_next_lucky_year(n):
    while True:
        n += 1
        if str(n).count('0') + str(n).count('1') == len(str(n)):
            return n - n + 1


# Read input from standard input
n = int(input().strip())

# Print the result
print(find_next_lucky_year(n))
