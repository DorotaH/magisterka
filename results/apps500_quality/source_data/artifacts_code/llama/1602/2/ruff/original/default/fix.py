import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    # Find the maximum element
    max_element = max(a)
    max_count = 0
    for x in a:
        if x == max_element:
            max_count += 1

    # If the maximum element is the only one, return it
    if max_count == n:
        print(max_element)
        return

    # Find the second maximum element
    second_max_element = max(x for x in a if x != max_element)

    # Create a new array with the maximum element first and the rest in any order
    new_a = [max_element] + sorted([x for x in a if x != max_element])

    # Initialize the result array
    result = []

    # Reorder the array to maximize the value of the array
    for i in range(n):
        if new_a[i] == second_max_element:
            result.append(new_a[i])
        else:
            result.append(a[i])

    # Print the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
