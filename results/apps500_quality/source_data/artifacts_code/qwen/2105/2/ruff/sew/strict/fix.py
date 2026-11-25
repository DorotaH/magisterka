def  get_year_name(n, m, s, t, q, queries):
    gapja = [s[i] + t[i] for i in range(min(n, m))]
    if n > m:
        gapja+=s[m:]
    elif n < m:
        gapja += t[n:]

    result = list()
    for y in queries:
        index=(y-1)%len(gapja)
        result.append(gapja[index])

    return result

# Read input
n, m=map(int, input().split())
s = input().split()
t = input().split()
q=int(input())
queries = []
for _ in range(q):
    queries.append(int(input()))

# Get the result
result=get_year_name(n, m, s, t, q, queries)

# Print the result
for name in result:
    print(name)
