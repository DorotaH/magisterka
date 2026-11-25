def can_form_good_string(s):
    from collections import Counter
    count = Counter(s)
    odd_count = sum(bool(v % 2 != 0)
                for v in count.values())
    return -1 if odd_count > 1 else s


def rearrange_to_good_string(s):
    from collections import Counter
    count = Counter(s)
    odd_chars = [char for char, freq in count.items() if freq % 2 != 0]
    even_chars = [char for char, freq in count.items() if freq % 2 == 0]

    if len(odd_chars) > 1:
        return -1

    if len(odd_chars) == 1:
        odd_char = odd_chars[0]
        even_char = even_chars[0]
        result = (len(even_chars) // 2) * [even_char] + [odd_char] + (len(even_chars) // 2) * [even_char]
    else:
        result = (len(even_chars) // 2) * [even_char]

    return ''.join(result)


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    queries = data[1:]

    results = []
    for query in queries:
        if len(query) == 1:
            results.append(-1)
        else:
            result = rearrange_to_good_string(query)
            results.append(result)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
