def split_sequence(n, a):
    if n == 1:
        return "YES\n0"
    increasing = []
    decreasing = []
    i = 0
    while i < n:
        if i + 1 < n and a[i] < a[i + 1]:
            increasing.append(a[i])
        else:
            decreasing.append(a[i])
        i += 1
        if i < n and increasing and decreasing and decreasing[-1] <= increasing[-1]:
            return "NO"
    return "".join("0" if x in increasing else "1" for x in a) + "YES\n"


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output result
result = split_sequence(n, a)
print(result)
