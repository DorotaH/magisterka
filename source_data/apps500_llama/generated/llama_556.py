# Read input from standard input
a, b, c = map(int, input().split())

# If C is 0, it's not possible to make the sum congruent to 0 modulo B
if c == 0:
    print("NO")
else:
    # Check if C is a multiple of A
    if c % a == 0:
        print("YES")
    else:
        # Find the remainder of C divided by A
        r = c % a
        # If the remainder is 0, it means C is congruent to 0 modulo A, so it's possible to make the sum congruent to C modulo B
        if r == 0:
            print("YES")
        else:
            # Check if the remainder is less than B
            if r < b:
                # If the remainder is not a multiple of B, it's not possible to make the sum congruent to C modulo B
                if (b - r) % a != 0:
                    print("NO")
                else:
                    print("YES")
            else:
                print("NO")
