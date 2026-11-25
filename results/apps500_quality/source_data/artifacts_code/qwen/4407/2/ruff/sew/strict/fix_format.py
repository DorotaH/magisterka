def min_coins_to_make_value(coins, value):
    if value == 0:
        return 0
    coins.sort(reverse=True)
    for i, coin in enumerate(coins):
        if coin <= value:
            return 1 + min_coins_to_make_value(coins[i + 1 :], value - coin)
    return -1


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    q = int(data[1])
    coins = list(map(int, data[2 : 2 + n]))
    queries = list(map(int, data[2 + n :]))

    results = [min_coins_to_make_value(coins, query) for query in queries]

    print(*results)


if __name__ == "__main__":
    main()
