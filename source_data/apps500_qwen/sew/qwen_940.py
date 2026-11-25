def  find_third_string(n, t, s1, s2):
    if t * 2>n:
        return -1
    
    s3 = list(s1)
    changes = 0
    
    for i in range(n):
        if  s1[i] != s2[i]:
            if changes < t:
                s3[i] = s2[i]
                changes += 1
            else:
                break
    
    if changes != t:
        return -1
    
    return  ''.join(s3)

# Read input
import  sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
t = int(data[1])
s1 = data[2]
s2 = data[3]

# Find and print the result
result = find_third_string(n, t, s1, s2)
print(result)
