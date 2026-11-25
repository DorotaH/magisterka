from collections import deque


def is_consistent(n, events):
    prices = deque(range(1, n + 1))
    placed = []
    
    for event in events:
        if event == '+':
            placed.append(prices[0])
        elif event.startswith('-'):
            price = int(event[1:])
            if not prices or prices[0] != price:
                return False
            placed.append(price)
            prices.popleft()
    
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    events = data[1:]
    
    if is_consistent(n, events):
        print("YES")
        prices = deque(range(1, n + 1))
        placed = []
        
        for event in events:
            if event == '+':
                placed.append(prices[0])
            elif event.startswith('-'):
                price = int(event[1:])
                placed.append(price)
                prices.popleft()
        
        print(' '.join(map(str, placed)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
