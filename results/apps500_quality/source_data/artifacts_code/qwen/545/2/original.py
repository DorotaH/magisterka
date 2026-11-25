def find_third_string(n, t, s1, s2):
    if t == n:
        return -1
    if t == 0:
        return s1
    
    diff_indices = []
    for i in range(n):
        if s1[i] != s2[i]:
            diff_indices.append(i)
    
    if len(diff_indices) < t:
        return -1
    
    s3 = list(s1)
    for i in range(t):
        s3[diff_indices[i]] = 'a' if s1[diff_indices[i]] == 'b' else 'b'
    
    return ''.join(s3)

# Read input
n, t = map(int, input().split())
s1 = input().strip()
s2 = input().strip()

# Find and print the third string
result = find_third_string(n, t, s1, s2)
print(result)
