a, b = [list(map(int, input().split())) for _ in range(4)]

first_defence, first_attack = max(a[0], a[1]), max(b[0], b[1])
second_defence, second_attack = max(a[2], a[3]), max(b[2], b[3])

if  second_defence < first_attack and  second_attack < first_defence:
    print("Team 1")
elif  second_defence > first_attack and second_attack > first_defence:
    print("Team 2")
else:
    print("Draw")