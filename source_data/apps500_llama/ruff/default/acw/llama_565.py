s = input().strip()
b_count = s.count("B")
w_count = s.count("W")

if w_count < b_count:
    print(b_count - w_count)
elif w_count > b_count:
    print(w_count - b_count)
else:
    print(0)
