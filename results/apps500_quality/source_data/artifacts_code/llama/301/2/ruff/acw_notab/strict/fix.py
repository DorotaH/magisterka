

def shortest_xor_sum_array():
    u, v = map(int, input().split())
    if v < u:
        print(-1)
        return

    if u == 0:
        print(0)
        return

    result = []
    power_of_two = 1
    while (power_of_two <= u):
        result.append(power_of_two)
        power_of_two <<= 1

    remaining = v - sum(result)
    while (power_of_two <= remaining):
        result.append(power_of_two)
        remaining -= power_of_two
        power_of_two >>= 1

    if (remaining != 0):
        print(-1)
        return

    print(len(result))
    print(*result)


if __name__ == "__main__":
    shortest_xor_sum_array()
