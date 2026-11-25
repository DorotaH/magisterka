def  min_sequence():
    n, sequence = int(input()), []
    current_num = 1
    for _ in range(n):
        b = int(input())
        while sum(int(digit) for digit in str(current_num)) != b:
            current_num += 1
        sequence.append(current_num)
        current_num = current_num + 1
    print('\n'.join(map(str, sequence)))

min_sequence()