a, b = [list(map(int, input().split())) for _ in range(4)]

first_defence = max(a[0], a[1])
first_attack = max(b[0], b[1])
second_defence = max(a[2], a[3])
second_attack = max(b[2], b[3])

if first_attack > second_defence and first_defence > second_attack:
    print("Team 1")
elif first_attack < second_defence and first_defence < second_attack:
    print("Team 2")
else:
    print("Draw")
