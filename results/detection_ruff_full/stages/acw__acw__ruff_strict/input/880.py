def Check_Solution(a, b, c):
    if ((b * b) - (a * 4 * c)) > 0:
        return "2 solutions"
    return "1 solution" if ((b * b) - (a * 4 * c)) == 0 else "No solutions"
