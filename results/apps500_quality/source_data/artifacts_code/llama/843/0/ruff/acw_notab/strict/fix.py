def find_infinite_jump(n, directions, jump_lengths):
    position = 1
    while True:
        if 1 <= position <= n:
            jump = jump_lengths[position - 1]
            if directions[position - 1] == '>':
                position += jump
            else:
                position -= jump
        else:
            break
    return "INFINITE" if position == 1 else "FINITE"


n = int(input())
directions = input()
jump_lengths = list(map(int, input().split()))

print(find_infinite_jump(n, directions, jump_lengths))
