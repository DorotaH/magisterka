import sys
input = sys.stdin.read
data = input().split()

a = data[0]
b = data[1]

a_list = list(a)
b_list = list(b)

a_list.sort(reverse=True)

i = 0
while i < len(a_list):
    if int(''.join(a_list[:i+1])) <= int(''.join(b_list[:i+1])):
        i += 1
    else:
        break

a_list[i], a_list[0] = a_list[0], a_list[i]

print(''.join(a_list))
