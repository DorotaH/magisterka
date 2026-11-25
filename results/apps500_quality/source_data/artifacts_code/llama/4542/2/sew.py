s=input().strip()


def find_min_stones(s):
    n, black_count = len(s), s.count('B')
    white_count = n - black_count

    if not black_count > white_count:
        return white_count - black_count
    else:
        return black_count - white_count

print(find_min_stones(s))
