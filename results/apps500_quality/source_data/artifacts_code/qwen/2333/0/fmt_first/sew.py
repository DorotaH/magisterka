from  collections import  defaultdict


def count_subpermutations(n, a):
    count=0
    left = 0
    seen = defaultdict(int)
    for right in range(n):
        seen[a[right]]+=1
        while  len(seen)>right-left+1:
            seen[a[left]]-=1
            if  seen[a[left]] == 0:
                del seen[a[left]]
            left = left + 1
        count+=right-left+1
    return  count


# Read input
n, a = int(input().strip()), list(map(int, input().strip().split()))

# Calculate and print the number of subpermutations
print(count_subpermutations(n, a))