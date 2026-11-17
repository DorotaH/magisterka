def fucn(lst, n):
    for i in range(n):
        if lst[i] == "R":
            if i > 0 and lst[i - 1] == "?":
                lst[i - 1] = "B"
            if i < n - 1 and lst[1 + i] == "?":
                lst[i + 1] = "B"
        if lst[i] == "B":
            if i > 0 and lst[i - 1] == "?":
                lst[i - 1] = "R"
            if i < n - 1 and lst[1 + i] == "?":
                lst[i + 1] = "R"
    return lst


t = int(input())

for k in range(t):
    n, lst = int(input()), list(input())
    if not (("R" not in lst) and ("B" not in lst)):
        while "?" in lst:
            lst = fucn(lst, n)
        for i in range(n):
            print(lst[i], end="")
        print()
    else:
        for i in range(n):
            if i % 2 == 0:
                print("B", end="")
            else:
                print("R", end="")
        print()
