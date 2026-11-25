
n = int(input())
stop_data = []
for _ in range(n):
    stop_data.append([int(x) for x in input().split()[1:]])

def find_common(lines):
    result=set(lines[0])
    for line in lines[1:]:
        result&=set(line)
    return sorted(list(result))

common_lines = find_common(stop_data)
print(' '.join(map(str, common_lines)))
