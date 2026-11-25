s = input()
heidi = "heidi"

def check_subsequence(s, heidi):
    s_pointer = 0
    heidi_pointer = 0
    while s_pointer<len(s) and heidi_pointer<len(heidi):
        if  s[s_pointer] == heidi[heidi_pointer]:
            heidi_pointer += 1
        s_pointer += 1
    return heidi_pointer==len(heidi)

print("YES" if check_subsequence(s, heidi) else "NO")
