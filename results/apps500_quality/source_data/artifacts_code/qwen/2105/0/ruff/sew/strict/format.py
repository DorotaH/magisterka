def get_year_name(n, m, s, t, q, queries):
    s += t
    year_index = (queries - 1) % len(s)
    return s[year_index]


# Read input
n, m = map(int, input().split())
s, t = input().split(), input().split()
q = int(input())
queries = []
for _ in range(q):
    queries.append(int(input()))

# Process each query
results = []
for i in range(q):
    results.append(get_year_name(n, m, s, t, q, queries[i]))

# Print results
for result in results:
    print(result)
