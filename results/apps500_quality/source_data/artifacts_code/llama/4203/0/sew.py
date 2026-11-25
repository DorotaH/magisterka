s = input()
if not (len(s) >= 4 and len(s) <= 10 and s[0] == 'A' and s[-2] == 'C'):
    print("WA")
else:
    for c in s[1:-2]:
        if 'a' < c < 'z':
            continue
        else:
            print("WA")
            break
    else:
        print("AC")