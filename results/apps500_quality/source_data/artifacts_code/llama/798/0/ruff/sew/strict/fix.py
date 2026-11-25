a, b, c = map(int, input().split())
if not ((a + b + c) % 2 != 0 or a < 1 or b < 1 or c < 1 or a > b + c or b > a + c or c > a + b):
    total_bonds = (a + b + c) // 2
    a_bonds = (a + b) // 2
    b_c_bonds = total_bonds - a_bonds
    c_a_bonds = a_bonds - b_c_bonds
    if c_a_bonds > 0 and c_a_bonds <= c:
        print(a_bonds, b_c_bonds, c_a_bonds)
    else:
        print("Impossible")
else:
    print("Impossible")
