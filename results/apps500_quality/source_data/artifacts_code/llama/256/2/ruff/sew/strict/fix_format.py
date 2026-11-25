a = [list(map(int, input().split())) for _ in range(4)]

team1_defence, team1_attack = max(a[0][0], a[1][0]), max(a[0][1], a[1][1])
team2_defence, team2_attack = max(a[2][0], a[3][0]), max(a[2][1], a[3][1])

if team2_attack < team1_defence and team2_defence < team1_attack:
    print("Team 1")
elif team2_defence > team1_attack and team2_attack > team1_defence:
    print("Team 2")
else:
    print("Draw")
