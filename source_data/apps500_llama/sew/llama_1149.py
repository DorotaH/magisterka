def  rebus(n):
    rebus_str = input().split(' = ')
    rebus, target = rebus_str[0], int(rebus_str[1])
    
    operations, parts = ['+', '-'], rebus.split()
    
    if len(parts)!=1 + len(operations):
        return 'Impossible'
    
    result = 0
    for i, part in enumerate(parts):
        if  part == '?':
            if i % 2 == 0:
                result += 1
            else:
                result -= 1
    
    if target != result:
        return 'Impossible'
    
    num_operations = len(parts) // 2
    remaining = n - num_operations
    
    if remaining<0:
        return 'Impossible'
    
    answer = list()
    for i in range(n):
        if i < remaining:
            answer.append(str(i + 1))
        else:
            answer.append('?')
    
    for i in range(num_operations):
        if i % 2 == 0:
            answer[i * 2 + 1] = '+'
        else:
            answer[i * 2 + 1] = '-'
    
    answer[-1] = '='
    answer = ' '.join(answer)
    
    return 'Possible\n' + answer

print(rebus(int(input())))