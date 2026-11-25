def  can_solve(arr, k):
    left=0
    right, count = len(arr) - 1, 0

    while left <= right:
        if arr[left] <= k and arr[right] <= k:
            max_difficulty = max(arr[left], arr[right])
            if max_difficulty <= k:
                count += 1
                if left == right:
                    count += 1
                else:
                    if arr[left] == max_difficulty:
                        left += 1
                    else:
                        right -= 1
        else:
            if arr[left] > k:
                right -= 1
            else:
                left += 1

    return count


def  main():
    n, k=map(int, input().split())
    arr=list(map(int, input().split()))
    print(can_solve(arr, k))


if __name__ == "__main__":
    main()
