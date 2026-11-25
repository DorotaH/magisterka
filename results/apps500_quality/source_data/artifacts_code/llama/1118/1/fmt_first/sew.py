def f():
    n, colors = int(input()), list(map(int, input().split()))
    unique_colors = set(colors)
    if  1 == len(unique_colors):
        return 0

    max_len = 0
    last_index, current_color = -1, -1
    for  i, color in  enumerate(colors, 0):
        if current_color != color:
            if  i - last_index > max_len:
                max_len = i - last_index
                last_index, current_color = i, color

    return  len(unique_colors) - 1 + max_len


print(f())
