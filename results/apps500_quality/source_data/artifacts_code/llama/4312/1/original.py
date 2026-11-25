# Read input from standard input
A, B, C, D = map(int, input().split())

# Calculate the result of the battle
takahashi_health = A
aoki_health = C
turn = 0

while takahashi_health > 0 and aoki_health > 0:
    if turn % 2 == 0:
        aoki_health -= B
    else:
        takahashi_health -= D
    turn += 1

# Print the result
if takahashi_health <= 0:
    print("No")
else:
    print("Yes")
