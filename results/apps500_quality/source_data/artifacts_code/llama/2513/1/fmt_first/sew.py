def is_possible(s):
    n=int(input())
    s, t = input(), ["" for _ in range(n)]

    # Check if s_i equals to the parity of the number of wolves in the group of i, i+1, i-1
    wolf_count=0
    for  i in  range(0, n):
        if  s[i]=="x":
            wolf_count = wolf_count + 1
        t[i] = "W" if  wolf_count % 2 else "S"

    # Check if the group of 1, 2, N, N-1 satisfies the condition
    group1, group2 = t[0] != t[1], t[-1] != t[-2]

    # Check if the group of 2, 1, N, N-1 satisfies the condition
    group3, group4 = t[1] != t[0], t[-2] != t[-1]

    return (group1 == group2 and group3 == group4) and all(
        s[i] == ("x" if t[(i + 1) % n] != t[i] else "o" for i in range(n))
        )


if not is_possible(input()):
    print(-1)
else:
    t = ["" for _ in range(int(input()))]
    wolf_count = 0
    for i in range(int(input())):
        if input() == "x":
            wolf_count += 1
        t[i] = "W" if wolf_count % 2 else "S"
    print("".join(t))
