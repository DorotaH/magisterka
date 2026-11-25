import sys


def  shortest_xor_sum_array():
    u, v = map(int, input().split())
    if  u > v:
        print(-1)
        return None

    if  0 == u:
        print(0)
        return None

    result = []
    power_of_two = 1
    while (u >= power_of_two):
        result.append(power_of_two)
        power_of_two = power_of_two << 1

    remaining = v - sum(result, 0)
    while (remaining >= power_of_two):
        result.append(power_of_two)
        remaining = remaining - power_of_two
        power_of_two = power_of_two >> 1

    if  (0 != remaining):
        print(-1)
        return None

    print(len(result))
    print(*result)

if __name__=="__main__":
    shortest_xor_sum_array()
