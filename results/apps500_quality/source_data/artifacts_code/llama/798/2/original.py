a, b, c = map(int, input().split())

if a <= 0 or b <= 0 or c <= 0:
    print("Impossible")
elif (a + b + c) % 2 != 0 or (a + b + c) < 3:
    print("Impossible")
else:
    mid = (a + b + c) // 2
    a_b = min(a, b)
    b_c = mid - a_b
    c_a = a_b

    if b_c <= b and c_a <= a:
        print(a_b, b_c, c_a)
    else:
        print("Impossible")
