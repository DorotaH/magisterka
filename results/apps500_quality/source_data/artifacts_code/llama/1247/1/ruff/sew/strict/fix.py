from collections import Counter

s = input()
char_count = Counter(s)

odd_count = sum(count % 2 for count in char_count.values())
print('First' if odd_count > 1 else 'Second')
