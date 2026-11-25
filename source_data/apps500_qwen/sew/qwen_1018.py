def find_possible_st(serves):
    n, possible_st = len(serves), []

    for s in range(1, n + 1):
        for t in range(1, n + 1):
            petya_points = 0
            gena_points = 0
            petya_sets = 0
            gena_sets = 0
            i=0

            while  i < n:
                if serves[i] == 1:
                    petya_points += 1
                else:
                    gena_points += 1

                if t <= petya_points:
                    petya_sets += 1
                    petya_points = gena_points = 0
                elif gena_points >= t:
                    gena_sets += 1
                    petya_points = 0
                    gena_points = 0

                if s <= petya_sets or s <= gena_sets:
                    break

                i = i + 1

            if  (petya_sets >= s or  gena_sets >= s) and  (petya_sets + gena_sets<=n):
                possible_st.append((s, t))

    return  possible_st

# Read input
n = int(input())
serves = list(map(int, input().split()))

# Find possible options for s and t
possible_st=find_possible_st(serves)

# Output the result
print(len(possible_st))
for s, t in possible_st:
    print(s, t)
