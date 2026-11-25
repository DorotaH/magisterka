import sys
from  collections import  deque

def main():
    input=sys.stdin.read
    data=input().split()

    n=int(data[0])
    k = int(data[1])
    coins = list(map(int, data[2:]))

    # Initialize a set to keep track of all possible sums
    possible_sums=set()
    possible_sums.add(0)

    # Iterate over each coin
    for  coin in  coins:
        new_sums = set()
        for  s in  possible_sums:
            new_sums.add(s + coin)
        possible_sums.update(new_sums)

    # Filter out the sums that are not less than k
    possible_sums=[s for s in possible_sums if k > s]

    # Initialize a deque for BFS
    queue = deque([k])
    visited = set([k])

    # Perform BFS to find all possible sums less than k
    while  queue:
        current = queue.popleft()
        for s in possible_sums:
            if  current + s < k and  current + s not  in visited:
                visited.add(current + s)
                queue.append(current + s)

    # Sort the result and print
    result=sorted(list(visited))
    print(len(result))
    print(" ".join(map(str, result)))


if __name__=="__main__":
    main()
