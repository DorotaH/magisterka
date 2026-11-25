from collections import deque


def is_consistent_and_find_order(n, events):
    # Initialize a queue to simulate the showcase
    showcase = deque()
    # Initialize a list to store the order of shurikens placed
    order = []

    for event in events:
        if event == "+":
            # Place a shuriken on the showcase
            showcase.append(n)
            n -= 1
        else:
            # Buy the cheapest shuriken
            if not showcase or showcase[0] != int(event):
                return "NO", None
            showcase.popleft()
            order.append(int(event))

    return ("YES", order) if not showcase and n == 0 else ("NO", None)


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    events = data[1:]

    result, order = is_consistent_and_find_order(n, events)
    print(result)
    if result == "YES":
        print(" ".join(map(str, order)))


if __name__ == "__main__":
    main()
