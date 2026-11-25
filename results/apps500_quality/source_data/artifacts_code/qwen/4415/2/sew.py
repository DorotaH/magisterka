def split_sequence(a):
    n = len(a)
    increasing = []
    decreasing = []
    
    # Try to find the increasing part
    i = 0
    while  n > i and  a[i] <= a[1 + i]:
        increasing.append(a[i])
        i += 1
    
    # Try to find the decreasing part starting from the end of the increasing part
    j = n - 1
    while  j >= 0 and  a[j] >= a[j - 1]:
        decreasing.append(a[j])
        j -= 1
    
    # If the indices do not match, it means the sequence cannot be split into increasing and decreasing parts
    if  i != j + 1:
        return "NO"
    
    # Return the increasing and decreasing parts
    return "YES\n{}\n{}\n{}\n{}".format(len(increasing), ' '.join(map(str, increasing)), len(decreasing), ' '.join(map(str, decreasing[::-1])))

# Read input
import  sys
input=sys.stdin.read
data=input().split()
n = int(data[0])
a = list(map(int, data[1:]))

# Print the result
print(split_sequence(a))