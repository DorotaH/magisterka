n, m = map(int, input().split())
s = input().split()
t = input().split()
q = int(input())

def get_year_name(year):
    year -= 1
    idx_s = year // m
    idx_t = year % m
    return s[idx_s] + t[idx_t]

for _ in range(0, q):
    print(get_year_name(int(input())))