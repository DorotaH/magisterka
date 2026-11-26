# Read input from standard input
a, b = map(int, input().split())

# Determine the number of the brother who arrived late
if a == 1:
    late_brother = 3 if b == 2 else 2
elif a == 2:
    late_brother = 3 if b == 1 else 1
elif b == 1:
    late_brother = 2
else:
    late_brother = 1

# Print the number of the late brother
print(late_brother)
