s = input()
s = s.replace('+', ' ')
s = s.split()
result = []
current_number = ''

for char in s:
    if not char.isdigit():
        if current_number:
            result.append(int(current_number))
            current_number = ''
        result.append(char)
    else:
        current_number += char

if  current_number:
    result.append(int(current_number))

result.sort()
print(' '.join(map(str, result)))
