def solve_rebus(rebus):
    operations = rebus.split()
    n = int(operations[-1])
    operations = operations[:-1]

    total = 0
    pos = 0
    for operation in operations:
        if operation == "+":
            total += 1
        elif operation == "-":
            total -= 1
        if 0 > total:
            return "Impossible"
        pos += 1

    total = 0
    pos = 0
    for operation in operations:
        if operation == "+":
            total += n - pos
        elif operation == "-":
            total -= n - pos
        if total != int(operations[-1]):
            return "Impossible"
        pos += 1

    return " ".join(operations).replace("?", str(n)) + "Possible\n"


rebus = input()
print(solve_rebus(rebus))
