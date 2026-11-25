# Read input from standard input
A, B, C, D = map(int, input().split())

# Check which way the balance scale tips
if  A+B>C+D:
    print("Left")
elif  A+B<C+D:
    print("Right")
else:
    print("Balanced")