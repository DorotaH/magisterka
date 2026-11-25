def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str():
    return input()


n = read_int()
a = read_int_list()

inc = []
dec = []
last_i, last_d = -1, -1
for i in range(n):
    if a[i] > last_i:
        inc.append(a[i])
        last_i = a[i]
    elif a[i] < last_d or last_i == -1 or last_d == -1:
        dec.append(a[i])
        last_d = a[i]
    elif a[i] == last_i:
        last_i = -1
        dec.append(a[i])
        last_d = a[i]
    else:
        print("NO")
        exit()

if last_i == -1 and last_d == -1:
    print("YES")
    print(0)
    print()
    print(0)
    print()
else:
    print("YES")
    print(len(inc))
    print(*inc)
    print(len(dec))
    print(*dec)
