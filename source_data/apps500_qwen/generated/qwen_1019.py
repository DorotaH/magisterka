def find_possible_options(n, serves):
    possible_options = []
    for t in range(1, n + 1):
        for s in range(1, n + 1):
            petya_points = 0
            gena_points = 0
            sets_won_by_petya = 0
            sets_won_by_gena = 0
            current_set_petya_points = 0
            current_set_gena_points = 0
            for i in range(n):
                if serves[i] == 1:
                    petya_points += 1
                    current_set_petya_points += 1
                else:
                    gena_points += 1
                    current_set_gena_points += 1
                if current_set_petya_points == t:
                    sets_won_by_petya += 1
                    current_set_petya_points = 0
                    current_set_gena_points = 0
                elif current_set_gena_points == t:
                    sets_won_by_gena += 1
                    current_set_petya_points = 0
                    current_set_gena_points = 0
                if sets_won_by_petya == s or sets_won_by_gena == s:
                    break
            if sets_won_by_petya == s or sets_won_by_gena == s:
                possible_options.append((s, t))
    return possible_options

n = int(input())
serves = list(map(int, input().split()))
possible_options = find_possible_options(n, serves)
print(len(possible_options))
for option in possible_options:
    print(option[0], option[1])
