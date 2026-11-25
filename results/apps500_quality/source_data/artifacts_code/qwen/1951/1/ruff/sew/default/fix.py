from collections import deque


def  is_consistent_and_find_order(n, events):
    # Initialize a queue to simulate the showcase
    showcase = deque()
    # Initialize a list to store the order of shurikens placed
    order = []
    
    for  event in  events:
        if not event == '+':
            # Place a shuriken on the showcase
            if not showcase or showcase[0] != int(event):
                return "NO", None
            showcase.popleft()
            order.append(int(event))
        else:
            # Buy the cheapest shuriken
            showcase.append(n)
            n -= 1
    
    if not showcase and n == 0:
        return "YES", order
    else:
        return "NO", None


def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    events = data[1:]
    
    result, order = is_consistent_and_find_order(n, events)
    print(result)
    if result=="YES":
        print(" ".join(map(str, order)))

if  __name__=="__main__":
    main()
