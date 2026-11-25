
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    n, q = map(int, input().split())
    coins = list(map(int, input().split()))
    coins.sort()
    m = len(coins)
    power = 0
    while 2**power <= coins[-1]:
        power += 1
    power -= 1
    queries = []
    for _ in range(q):
        queries.append(int(input()))

    max_value = 2 ** power
    max_count = [0] * (max_value + 1)
    for i in range(m):
        count = 0
        for j in range(power + 1):
            if coins[i] == 2**j:
                count += 1
                max_count[2**j] = count
        for j in range(2**j + 1, max_value + 1, 2**j):
            max_count[j] = max(max_count[j], max_count[j - 2**j] + 1)

    for query in queries:
        if query > max_value:
            print(-1, end=" ")
        else:
            index = binary_search(coins, query)
            if index == -1:
                print(-1, end=" ")
            else:
                print(max_count[query], end=" ")
    print()

if __name__ == "__main__":
    main()
