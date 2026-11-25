a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())

# Calculate the maximum possible defence and attack for each team
max_defense_team1 = max(a1, a2)
max_attack_team1 = max(b1, b2)
max_defense_team2 = max(a3, a4)
max_attack_team2 = max(b3, b4)

# Determine the winner based on the optimal strategies
if max_defense_team1 > max_attack_team2 and max_attack_team1 > max_defense_team2:
    print("Team 1")
elif max_defense_team2 > max_attack_team1 and max_attack_team2 > max_defense_team1:
    print("Team 2")
else:
    print("Draw")
