def can_reconstruct(n, a, k, b):
    queue = []
    for i in range(n):
        queue.append((a[i], i + 1))

    final_queue = []
    for i in range(k):
        final_queue.append((b[i], i + 1))

    final_queue.sort()

    actions = []
    while len(queue) > len(final_queue):
        if queue[0][0] < queue[1][0]:
            actions.append((1, 'R'))
            queue.pop(1)
        elif queue[-1][0] < queue[-2][0]:
            actions.append((len(queue), 'L'))
            queue.pop(-2)
        else:
            return "NO"

    for i in range(len(final_queue)):
        if queue[i][0] != final_queue[i][0] or queue[i][1] != final_queue[i][1]:
            return "NO"

    return "YES"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:]))

    result = can_reconstruct(n, a, k, b)
    print(result)
    if result == "YES":
        for action in actions:
            print(action[0], action[1])

if __name__ == "__main__":
    main()
