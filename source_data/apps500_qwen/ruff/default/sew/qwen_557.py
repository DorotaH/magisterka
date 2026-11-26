A, B, C = map(int, input().split())

# Check if C is already congruent to 0 modulo B
if not C == 0:
    if A % B == C:
        print("YES")
    else:
        print("NO")
else:
    # Check if there exists a multiple of A that is congruent to C modulo B
    print("YES")
