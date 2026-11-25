def can_transform(s, t, p):
    # Check if the length of s can be transformed to the length of t
    if len(s) != len(t):
        return "NO"

    # Count the frequency of each character in s, t, and p
    from collections import Counter

    count_s = Counter(s)
    count_t = Counter(t)
    count_p = Counter(p)

    # Check if s can be transformed to t by using characters from p
    for char in count_s:
        if count_s[char] > count_t[char]:
            if count_p[char] >= count_s[char] - count_t[char]:
                count_p[char] -= count_s[char] - count_t[char]
                count_s[char] = count_t[char]
            else:
                return "NO"

    # Check if all characters in count_p are used up
    if not sum(count_p.values()) == 0:
        return "NO"
    else:
        return "YES"


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    q = int(data[0])
    index = 1
    results = []

    for _ in range(0, q):
        s = data[index]
        index += 1
        t = data[index]
        index += 1
        p = data[index]
        index += 1
        results.append(can_transform(s, t, p))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
