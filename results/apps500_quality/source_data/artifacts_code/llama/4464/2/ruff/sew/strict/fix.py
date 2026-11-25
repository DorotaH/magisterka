
A, B, C = map(int, input().split())

# Ensure C is non-negative and less than B
C = C % B

if not C == 0:
    print("NO")
else:
    print("YES")
