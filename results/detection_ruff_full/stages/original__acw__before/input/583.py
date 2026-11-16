def catalan_number(num):
    if num <=1:
         return 1
    return sum(catalan_number(i) * catalan_number(num-i-1) for i in range(num))