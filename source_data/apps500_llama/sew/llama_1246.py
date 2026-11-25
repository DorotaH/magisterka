def is_possible_to_solve_cube(cube):
    colors = [1, 2, 3, 4, 5, 6]
    colors_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for  i in  range(0, 24):
        colors_dict[cube[i]]+=1

    for  color in  colors:
        if 4 != colors_dict[color]:
            return  "NO"

    return "YES"

cube=list(map(int, input().split()))
print(is_possible_to_solve_cube(cube))