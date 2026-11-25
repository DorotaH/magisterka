def lucky_number_index():
    n = int(input())
    lucky_nums = []
    i = 1
    while True:
        str_i = str(i)
        if all(digit in "47" for digit in str_i):
            lucky_nums.append(i)
        if i == n:
            return lucky_nums.index(i) + 1
        i += 1


print(lucky_number_index())
