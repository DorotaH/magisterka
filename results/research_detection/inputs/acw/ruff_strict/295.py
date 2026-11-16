def sum_div(number):
    divisors = [1]
    divisors.extend(i for i in range(2, number) if (number % i) == 0)
    return sum(divisors)
