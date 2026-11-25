S = input()
if S and S[0] == 'A' and len(S) >= 4 and len(S) <= 10:
    c_index = -1
    for i in range(2, len(S) - 1):
        if S[i] == 'C':
            c_index = i
            break
    if c_index != -1:
        is_all_lower = True
        for i in range(1, c_index) + range(c_index + 1, len(S) - 1):
            if S[i] != 'A' and not S[i].islower():
                is_all_lower = False
                break
        if c_index != 2 and c_index != len(S) - 2 and is_all_lower:
            print("AC")
        else:
            print("WA")
    else:
        print("WA")
else:
    print("WA")