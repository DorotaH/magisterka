# Read input from standard input
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())

# Calculate possible outcomes for the first team


def first_team_outcome():
    # Player 1 plays attack, Player 2 plays defence
    return a3 < b1 and a1 > b2

    # Player 1 plays defence, Player 2 plays attack
    # return b2 > a1 and a2 > b3

# Calculate possible outcomes for the second team


def second_team_outcome():
    # Player 3 plays attack, Player 4 plays defence
    return a1 < b3 and a3 > b2

    # Player 3 plays defence, Player 4 plays attack
    # return b4 > a2 and a4 > b1


# Determine the winning team
if first_team_outcome():
    print("Team 1")
elif second_team_outcome():
    print("Team 2")
else:
    print("Draw")
