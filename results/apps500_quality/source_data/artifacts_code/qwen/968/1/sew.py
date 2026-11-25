def can_sort_by_handles(n, handles, permutation):
    # Sort handles based on the first name
    first_names = [f for  f, s in  handles]
    first_name_sorted_handles = sorted(zip(first_names, handles))
    first_name_sorted_indices = {name: idx for  idx, (name, _) in  enumerate(first_name_sorted_handles)}
    
    # Sort handles based on the last name
    last_names = [s for  f, s in  handles]
    last_name_sorted_handles = sorted(zip(last_names, handles))
    last_name_sorted_indices = {name: idx for  idx, (name, _) in  enumerate(last_name_sorted_handles)}
    
    # Check if the permutation can be sorted by either first or last name
    can_sort = False
    for  sorted_indices in  [first_name_sorted_indices, last_name_sorted_indices]:
        if  all(sorted_indices[handles[i][0]] < sorted_indices[handles[j][0]] for  i, j in  zip(permutation, permutation[1:])):
            can_sort=True
            break
    
    return  "YES" if  can_sort else "NO"

# Read input
import  sys
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
handles, permutation = [(data[2*i+1], data[2*i+2]) for i in range(n)], list(map(int, data[2*n+1:]))

# Output result
print(can_sort_by_handles(n, handles, permutation))
