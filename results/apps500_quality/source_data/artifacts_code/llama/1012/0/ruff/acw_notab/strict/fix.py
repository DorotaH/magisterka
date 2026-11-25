from collections import Counter


def can_make_good_string(s):
    char_count = Counter(s)

    odd_count = sum(bool(count % 2 != 0)
                for count in char_count.values())
    if odd_count > 1:
        return -1
    result = ''
    for char, count in char_count.items():
        result += (count // 2) * char

        if count % 2 != 0:
            if odd_count == 1:
                result += char
            else:
                return -1

    return result[::-1] if result == result[::-1] else result


t = int(input())
for _ in range(t):
    s = input()
    print(can_make_good_string(s))
