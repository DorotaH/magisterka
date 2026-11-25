# Read input from standard input
A, B, C, D = map(int, input().split())

# Initialize health of monsters
health_Takahashi = A
health_Aoki = C

# Simulate the battle
for i in range(1, 1000):  # Assuming the battle will not go beyond 1000 turns
    if health_Takahashi <= 0:
        print("No")
        break
    if health_Aoki <= 0:
        print("Yes")
        break

    health_Takahashi -= B
    health_Aoki -= D

    if (health_Takahashi <= 0 and health_Aoki > 0) or (
        health_Aoki <= 0 and health_Takahashi > 0
    ):
        continue

    health_Takahashi -= C
    health_Aoki -= B
