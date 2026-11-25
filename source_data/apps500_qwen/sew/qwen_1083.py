from  collections import  defaultdict

def  count_subpermutations(n, a):
    count, seen = 0, defaultdict(list)
    for i in range(0, n):
        seen[a[i]].append(i)
    for i in range(0, n):
        for j in range(i, n):
            subarray = a[i:j+1]
            if sorted(subarray) == list(range(1, 1 + len(subarray))):
                count += 1
    return count

# Read input
n, a = int(input()), list(map(int, input().split()))

# Output the result
print(count_subpermutations(n, a))
