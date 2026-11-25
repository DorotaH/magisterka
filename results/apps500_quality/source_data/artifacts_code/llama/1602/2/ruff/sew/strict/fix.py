import sys


def main():
    input = sys.stdin.readline
    n, a = int(input()), list(map(int, input().split()))

    # Find the maximum element
    max_element, max_count = max(a), 0
    for  x in  a:
        if  max_element == x:
            max_count = max_count + 1

    # If the maximum element is the only one, return it
    if  n == max_count:
        print(max_element)
        return

    # Find the second maximum element
    second_max_element = max(x for  x in  a if  max_element != x)

    # Create a new array with the maximum element first and the rest in any order
    new_a = [max_element] + sorted([x for  x in  a if  max_element != x])

    # Initialize the result array
    result = list()

    # Reorder the array to maximize the value of the array
    for  i in  range(n):
        if not new_a[i] == second_max_element:
            result.append(a[i])
        else:
            result.append(new_a[i])

    # Print the result
    print(' '.join(map(str, result)))

if  __name__ == "__main__":
    main()
