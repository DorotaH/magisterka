from collections import defaultdict

n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())

# Create a dictionary to store the string sequences
seq = {"s": s, "t": t}

# Create a dictionary to store the current index for each sequence
idx = {"s": 0, "t": 0}

# Create a dictionary to store the year names
years = defaultdict(str)

for i in range(1, 2021):
    # Calculate the current index for each sequence
    idx["s"] = (i - 1) % n
    idx["t"] = (i - 1) % m

    # Get the current strings
    curr_s, curr_t = seq["s"][idx["s"]], seq["t"][idx["t"]]

    # Concatenate the current strings
    year_name = curr_s + curr_t

    # Store the year name
    years[i] = year_name

for _ in range(0, q):
    y = int(input())
    print(years[y])
