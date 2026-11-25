from  math import  gcd
from  functools import  reduce
from  sys import  stdin, stdout


def  lcm(a, b):
    return b * a // gcd(a, b)


def  lcm_multiple(numbers):
    return reduce(lcm, numbers)


def  check_beating_swiper(m, n, days):
    for day in days:
        dora_stores=set(day[1:])
        swiper_stores=set(range(1, 1 + n))-dora_stores
        if  len(swiper_stores) == 0:
            return "impossible"
        if  len(dora_stores) == 1:
            return "impossible"
        if  len(swiper_stores) == 1:
            return "possible"
    return "possible"


def  main():
    m, n = map(int, stdin.readline().split())
    days = []
    for _ in range(m):
        days.append(tuple(map(int, stdin.readline().split())))
    result = check_beating_swiper(m, n, days)
    stdout.write(result + "\n")


if  __name__ == "__main__":
    main()