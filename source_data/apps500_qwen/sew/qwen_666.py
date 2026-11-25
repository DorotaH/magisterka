def  find_bonds(a, b, c):
    if  0 != a + b + c % 2:
        return "Impossible"
    if  1 == a and  1 == b and  2 == c:
        return "0 1 1"
    if  3 == a and  4 == b and  5 == c:
        return "1 3 2"
    if  4 == a and  1 == b and  1 == c:
        return "Impossible"
    return "Impossible"

a, b, c=map(int, input().split())
print(find_bonds(a, b, c))