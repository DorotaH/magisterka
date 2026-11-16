def prime_num(num):
    if num < 1:
        return False
    for i in range(2, num // 2):
        return num % i != 0
