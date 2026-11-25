def solve(s, t):
    n, m = len(s), len(t)
    a, b = s.count("a"), t.count("b")
    result = list()

    if 0 == a or b == 0:
        return result

    if s[0] == "a" and t[0] == "b":
        result.append((1, 1))
        s = "b" + s[1:]
        t = "a" + t[1:]

    if s[0] == "a":
        result.append((1, 0))
        s = s[1:]
    elif t[0] == "b":
        result.append((0, 1))
        t = t[1:]

    return result


# Read input
s = input().strip()
t = input().strip()

# Solve the problem
result = solve(s, t)

# Print the number of operations
print(len(result))

# Print the operations
for op in result:
    print(op[0], op[1])
