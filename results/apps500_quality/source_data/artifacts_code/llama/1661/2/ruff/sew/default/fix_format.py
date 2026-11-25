import sys


def can_buy_game(game_cost, bills):
    """Return True if game_cost can be bought from bills."""
    if not bills:
        return False
    return bills[0] >= game_cost


def main():
    n, m = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    a = list(map(int, sys.stdin.readline().split()))

    games_bought = i = 0
    j = 0

    while i < n and j < m:
        if can_buy_game(c[i], a):
            games_bought += 1
            j += 1
        i += 1

    print(games_bought)


if __name__ == "__main__":
    main()
