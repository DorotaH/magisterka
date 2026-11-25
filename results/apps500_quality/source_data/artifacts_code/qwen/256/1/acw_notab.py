import sys
input = sys.stdin.read
data = input().split()

a1, b1 = int(data[0]), int(data[1])
a2, b2 = int(data[2]), int(data[3])
a3, b3 = int(data[4]), int(data[5])
a4, b4 = int(data[6]), int(data[7])

# Calculate the possible outcomes for both teams
# Team 1's possible outcomes
team1_win = (a3 < b1 and a1 > b3) or (b1 > a4 and a1 > b4)
team1_draw = (b1 == a3 and a1 == b3) or (b1 == a4 and a1 == b4)

# Team 2's possible outcomes
team2_win = (a1 < b2 and b1 < a2) or (a3 < b2 and b3 < a2)
team2_draw = (b2 == a1 and a2 == b1) or (b2 == a3 and a2 == b3)

# Determine the result
if team1_win:
    print("Team 1")
elif team2_win:
    print("Team 2")
else:
    print("Draw")
