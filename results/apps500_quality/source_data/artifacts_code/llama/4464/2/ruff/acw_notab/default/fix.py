
A, B, C = map(int, input().split())

# Ensure C is non-negative and less than B
C = C % B

if C == 0:
    print("YES")
else:
    print("NO")
