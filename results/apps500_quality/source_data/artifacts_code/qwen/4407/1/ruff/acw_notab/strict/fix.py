def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    q = int(data[1])

    coins = list(map(int, data[2:2 + n]))
    queries = list(map(int, data[2 + n:2 + n + q]))

    # Create a dictionary to count the occurrences of each coin value
    coin_count = {}
    for coin in coins:
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1

    answers = []
    for query in queries:
        if query == 0:
            answers.append(0)
        elif query in coin_count:
            answers.append(1)
        else:
            min_coins = float('inf')
            # Check all combinations of coins to find the minimum number of coins needed
            for i in range(1, 1 << n):
                total = 0
                count = 0
                for j in range(n):
                    if i & (1 << j):
                        total += coins[j]
                        count += 1
                if total == query:
                    min_coins = min(min_coins, count)
            if min_coins == float('inf'):
                answers.append(-1)
            else:
                answers.append(min_coins)

    # Print the answers
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()
