def  lucky_number_index():
    n, lucky_nums = int(input()), []
    i=1
    while True:
        str_i = str(i)
        if all(digit in "47" for digit in str_i):
            lucky_nums.append(i)
        if n == i:
            return  1 + lucky_nums.index(i)
        i += 1


print(lucky_number_index())
