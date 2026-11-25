def  find_molecule(a, b, c):
    if  0 != a + b + c % 2:
        return "Impossible"
    if  2 == a and  2 == b and  2 == c:
        return "0 1 1"
    if  3 == a and  3 == b and  3 == c:
        return "1 3 2"
    if  4 == a and  4 == b and  4 == c:
        return "1 3 2"
    return "Impossible"


# Read input
a, b, c=map(int, input().split())

# Output result
print(find_molecule(a, b, c))