def solve():
    n, m = map(int, input().split())
    prices = []
    for _ in range(n):
        a, b = map(int, input().split())
        prices.append((a / b, m))

    min_cost = float("inf")
    for price, num in prices:
        cost = price * num
        min_cost = min(min_cost, cost)

    print(f"{min_cost:.8f}")


if __name__ == "__main__":
    solve()
