import sys
from collections import Counter


def can_form_good_string(s):
    count = Counter(s)
    odd_count = sum(bool(v % 2 != 0)
                for v in count.values())
    return odd_count <= 1


def rearrange_to_good_string(s):
    if not can_form_good_string(s):
        return -1
    count = Counter(s)
    odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
    even_chars = [char for char, freq in count.items() if freq % 2 == 0]
    odd_chars.sort()
    even_chars.sort()
    result = even_chars + odd_chars
    return ''.join(result)


def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(t):
        s = data[i + 1]
        result = rearrange_to_good_string(s)
        results.append(result)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
