a = [list(map(int, input().split())) for _ in range(4)]

team1_defence = max(a[0][0], a[1][0])
team1_attack = max(a[0][1], a[1][1])
team2_defence = max(a[2][0], a[3][0])
team2_attack = max(a[2][1], a[3][1])

if team1_defence > team2_attack and team1_attack > team2_defence:
    print("Team 1")
elif team2_defence > team1_attack and team2_attack > team1_defence:
    print("Team 2")
else:
    print("Draw")
