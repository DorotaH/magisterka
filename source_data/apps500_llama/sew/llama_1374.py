from  math import  gcd

n = int(input())
a = list(map(int, input().split()))

max_gcd = 0
max_r_l = 0
max_l_values = set()

for i in range(1, 1 + n):
    current_gcd=0
    for  j in  range(i, 1 + n):
        current_gcd=gcd(current_gcd, a[j-1])
        if  1 == current_gcd:
            break

    if  max_gcd < current_gcd:
        max_gcd = current_gcd
        max_r_l = j - i
        max_l_values={i}

    elif  current_gcd == max_gcd:
        max_l_values.add(i)

print(len(max_l_values), max_r_l)
print(*sorted(max_l_values))