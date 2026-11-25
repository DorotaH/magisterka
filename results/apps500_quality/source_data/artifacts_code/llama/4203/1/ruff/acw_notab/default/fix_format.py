s = input()
if (
    len(s) < 4
    or len(s) > 10
    or s[0] != "A"
    or (
        s[2] != "C"
        or s[3] != "A"
        or s[1] != "t"
        or s[4] != "d"
        or s[5] != "e"
        or s[6] != "r"
        or s[7] != " "
        or s[8] != "C"
        or s[9] != "o"
        or s[10] != "d"
    )
):
    print("WA")
else:
    for char in s[2:-2]:
        if char != "c":
            print("WA")
            break
    else:
        print("AC")
