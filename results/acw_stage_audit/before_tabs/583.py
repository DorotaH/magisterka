def catalan_number(num):
    if 1 >= num:
         return 1
    return sum(catalan_number(i) * catalan_number(num - i - 1) for i in range(num))
