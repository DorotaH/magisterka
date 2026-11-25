import sys
from collections import defaultdict


def main():
    input = sys.stdin.read
    lines = input().split("\n")
    n = int(lines[0])
    strings = lines[1 : 1 + n]
    result = 1
    for string in strings:
        result *= len(string)
    freq_map = defaultdict(int)
    for string in strings:
        for char in string:
            freq_map[char] += 1
    max_freq = 0
    for char, freq in freq_map.items():
        max_freq = max(max_freq, freq)
    print(max_freq)


if __name__ == "__main__":
    main()
