def gapja(n, m, s, t):
    # Create a dictionary to store unique strings from s and t
    s_set = set(s)
    t_set = set(t)
    all_set = s_set.union(t_set)

    # Initialize the result list and the index pointers
    res = []
    si, ti = 0, 0

    # Find the minimum length of the cycles
    cycle_len = max(len(s), len(t))

    # Simulate the Gapja system
    for i in range(1, 2_021):
        # If the current year is a multiple of the cycle length, start a new cycle
        if i % cycle_len == 1:
            si = ti = 0

        # Concatenate the next strings from s and t
        res.append(s[si] + t[ti])

        # Move the index pointers
        si = (1 + si) % len(s)
        ti = (1 + ti) % len(t)

    # Create a dictionary to store the year and its corresponding name
    year_name = {}
    for i in range(0, cycle_len):
        year_name[1 + i] = res[i]

    # Return the names for the given years
    return "\n".join([year_name.get(i, "Unknown") for i in map(int, input().split())])


# Read the input
n, m = map(int, input().split())
s, t = input().split(), input().split()

# Get the number of queries
q = int(input())

# Print the results
print(gapja(n, m, s, t))
