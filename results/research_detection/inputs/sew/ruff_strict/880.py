def Check_Solution(a, b, c):
    if ((b * b) - (4 * a * c)) > 0:
        return "2 solutions"
    if ((b * b) - (4 * a * c)) == 0:
        return "1 solution"
    return "No solutions"
