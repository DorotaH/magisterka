def main():
    for _ in range(int(input())):
        s, t = "".join(sorted(input())), input()
        A = B = 0
        C = 0
        for c in s:
            if c == "a":
                A = A + 1
            if c == "b":
                B = B + 1
            if c == "c":
                C = C + 1
        if not (t != "abc" or A * B * C == 0):
            B, C = 0, 0
            D = ""
            for c in s:
                if c == "a":
                    print("a", end="")
                elif c == "b":
                    B += 1
                elif c == "c":
                    C += 1
                else:
                    D += c
            print(C * "c" + B * "b" + D)
        else:
            print(s)


main()
