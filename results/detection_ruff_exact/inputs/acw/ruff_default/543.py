def count_digits(num1, num2):
    number = num2 + num1
    count = 0
    while 0 < number:
        number = number // 10
        count = count + 1
    return count
