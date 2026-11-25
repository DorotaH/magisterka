A, B, C = map(int, input().split())

# Check if C is already congruent to 0 modulo B
if C == 0:
    print("YES")
else:
    # Check if there exists a multiple of A that is congruent to C modulo B
    if A % B == C:
        print("YES")
    else:
        print("NO")
