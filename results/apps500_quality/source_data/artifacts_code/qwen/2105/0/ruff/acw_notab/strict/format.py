def get_year_name(n, m, s, t, q, queries):
    s += t
    year_index = (queries - 1) % len(s)
    return s[year_index]


# Read input
n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())
queries = [int(input()) for _ in range(q)]

# Process each query
results = [get_year_name(n, m, s, t, q, queries[i]) for i in range(q)]

# Print results
for result in results:
    print(result)
