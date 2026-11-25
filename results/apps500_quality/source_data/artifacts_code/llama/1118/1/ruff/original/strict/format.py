def f():
    n = int(input())
    colors = list(map(int, input().split()))
    unique_colors = set(colors)
    if len(unique_colors) == 1:
        return 0

    max_len = 0
    last_index = -1
    current_color = -1
    for i, color in enumerate(colors):
        if color != current_color:
            if i - last_index > max_len:
                max_len = i - last_index
                last_index = i
                current_color = color

    return len(unique_colors) - 1 + max_len


print(f())
