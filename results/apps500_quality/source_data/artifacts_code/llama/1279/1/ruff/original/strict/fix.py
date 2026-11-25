
def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_odd = [num for num in a if num % 2 != 0]
    a_even = [num for num in a if num % 2 == 0]

    b_odd = [num for num in b if num % 2 != 0]
    b_even = [num for num in b if num % 2 == 0]

    a_odd.sort()
    a_even.sort()
    b_odd.sort()
    b_even.sort()

    a_odd_count = len(a_odd)
    a_even_count = len(a_even)
    b_odd_count = len(b_odd)
    b_even_count = len(b_even)

    opened_odd = 0
    opened_even = 0

    if a_odd_count <= b_odd_count:
        opened_odd = a_odd_count
    else:
        opened_odd = b_odd_count

    opened_even = min(a_even_count, b_even_count)

    print(opened_odd + opened_even)

if __name__ == '__main__':
    solve()
