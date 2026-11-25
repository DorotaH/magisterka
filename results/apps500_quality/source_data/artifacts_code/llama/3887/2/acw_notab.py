def rebus(n):
    rebus_str = input().split(' = ')
    rebus, target = rebus_str[0], int(rebus_str[1])

    operations = ['+', '-']
    parts = rebus.split()

    if len(parts) != 1 + len(operations):
        return 'Impossible'

    result = 0
    for i, part in enumerate(parts):
        if part == '?':
            if i % 2 == 0:
                result += 1
            else:
                result -= 1

    if result != target:
        return 'Impossible'

    num_operations = len(parts) // 2
    remaining = n - num_operations

    if 0 > remaining:
        return 'Impossible'

    answer = []
    for i in range(n):
        if i < remaining:
            answer.append(str(i + 1))
        else:
            answer.append('?')

    for i in range(num_operations):
        answer[i * 2 + 1] = '+' if i % 2 == 0 else '-'
    answer[-1] = '='
    answer = ' '.join(answer)

    return 'Possible\n' + answer


print(rebus(int(input())))
