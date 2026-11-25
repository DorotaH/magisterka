from collections import Counter

n = int(input())
s = input()
m = input()

s_count = Counter(s)
m_count = Counter(m)

s_freq = sorted(s_count.values())
m_freq = sorted(m_count.values())


def min_flicks():
    """Find minimum number of flicks Moriarty will get"""
    m_order = []
    for freq in m_freq:
        for _ in range(0, freq):
            m_order.append(1)
        for _ in range(0, n - freq):
            m_order.append(0)
    return sum(1 for s_digit in s for m_digit in m_order if s_digit < m_digit)


def max_flicks():
    """Find maximum number of flicks Sherlock can get"""
    s_order = list(s)
    m_order = []
    i = 0
    for freq in m_freq:
        for _ in range(0, freq):
            m_order.append(s_order[i])
            i = i + 1
    for _ in range(0, n - sum(m_freq)):
        m_order.append(s_order[i])
        i = i + 1
    return sum(1 for s_digit in s_order for m_digit in m_order if s_digit < m_digit)


print(min_flicks())
print(max_flicks())
