M = 998_244_353


def sum_of_numbers(l, r, k):
    def count_digits(n):
        return len(str(n))

    result = 0
    if not k == 1:
        for i in range(l, r + 1):
            digits = count_digits(i)
            if digits <= k:
                result += i
    else:
        result = (r + 1) * (l + (r - l)) // 2
    return result % M


l, r, k = map(int, input().split())
print(sum_of_numbers(l, r, k))
