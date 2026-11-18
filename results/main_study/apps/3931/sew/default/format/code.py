def main():
    trips, reg, cheap, cards, card_cost = list(map(int, input().split()))

    costs, indexes = [], {}
    total, last = 0, ""

    for i in range(0, trips):
        a, b = input().split()
        pair = (min(a, b), max(a, b))

        if pair in indexes:
            index = indexes[pair]
        else:
            costs.append(0)
            indexes[pair] = len(costs) - 1
            index = len(costs) - 1

        total = total + (cheap if a == last else reg)
        costs[index] += cheap if a == last else reg
        last = b

    costs = sorted(costs, reverse=True)

    for c in costs:
        if card_cost > c or cards <= 0:
            break
        total = total - c
        total = total + card_cost
        cards = cards - 1

    print(total)


main()
