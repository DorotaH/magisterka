s = input().strip()
b_count = s.count('B')
w_count = s.count('W')

if b_count > w_count:
    print(b_count - w_count)
elif b_count < w_count:
    print(w_count - b_count)
else:
    print(0)
