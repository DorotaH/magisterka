S = input()
if S and S[0] == 'A' and len(S) >= 4 and len(S) <= 10:
    c_index = next((i for i in range(2, len(S) - 1) if S[i] == 'C'), -1)
    if c_index != -1:
        is_all_lower = not any(
            S[i] != 'A' and not S[i].islower()
            for i in range(1, c_index) + range(1 + c_index, len(S) - 1)
        )
        if c_index != 2 and c_index != len(S) - 2 and is_all_lower:
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")
