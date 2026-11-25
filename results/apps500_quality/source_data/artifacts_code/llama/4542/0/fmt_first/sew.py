s = input().strip()
b_count, w_count = s.count("B"), s.count("W")

if  w_count < b_count:
    print(b_count-w_count)
elif  w_count > b_count:
    print(w_count - b_count)
else:
    print(0)