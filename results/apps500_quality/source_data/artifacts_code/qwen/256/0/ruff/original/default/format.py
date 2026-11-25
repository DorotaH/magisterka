# Read input
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())

# Calculate the possible outcomes
# Team 1 can win if:
# - Player 1 plays attack and Player 2 plays defence, or
# - Player 2 plays attack and Player 1 plays defence
team1_wins = (max(a1, a2) > min(b3, b4) and min(b1, b2) > max(a3, a4)) or (
    max(a2, a1) > min(b3, b4) and min(b2, b1) > max(a3, a4)
)

# Team 2 can win if:
# - Player 3 plays attack and Player 4 plays defence, or
# - Player 4 plays attack and Player 3 plays defence
team2_wins = (max(a3, a4) > min(b1, b2) and min(b3, b4) > max(a1, a2)) or (
    max(a4, a3) > min(b1, b2) and min(b4, b3) > max(a1, a2)
)

# Determine the result
if team1_wins:
    print("Team 1")
elif team2_wins:
    print("Team 2")
else:
    print("Draw")
