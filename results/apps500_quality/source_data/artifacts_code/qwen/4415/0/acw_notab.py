def split_sequence(a):
    n = len(a)
    increasing = []
    decreasing = []
    
    for i in range(n):
        if not increasing or a[i] > increasing[-1]:
            increasing.append(a[i])
        elif not decreasing or decreasing[-1] < a[i]:
            decreasing.append(a[i])
        else:
            return "NO", [], []
    
    return "YES", increasing, decreasing


# Read input
n = int(input())
a = list(map(int, input().split()))

# Split the sequence
result, increasing, decreasing = split_sequence(a)

# Print output
print(result)
print(len(increasing))
if increasing:
    print(' '.join(map(str, increasing)))
print(len(decreasing))
if decreasing:
    print(' '.join(map(str, decreasing)))
