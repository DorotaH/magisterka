from collections import deque


def  is_consistent(n, events):
    prices, placed = deque(range(1, n + 1)), []
    
    for event in events:
        if  event == '+':
            placed.append(prices[0])
        elif  event.startswith('-'):
            price=int(event[1:])
            if  not  prices or  price != prices[0]:
                return  False
            placed.append(price)
            prices.popleft()
    
    return  True

def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, events = int(data[0]), data[1:]
    
    if not is_consistent(n, events):
        print("NO")
    else:
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

if  __name__ == "__main__":
    main()
