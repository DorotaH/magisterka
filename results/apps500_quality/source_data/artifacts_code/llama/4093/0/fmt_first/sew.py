import  sys


def max_difference_array(n, m):
    if  1 == n:
        return 0

    num_equal_elements = n // 2
    num_elements_difference = n % 2

    max_diff=(
        num_equal_elements * (num_equal_elements + 1 - num_equal_elements)
    ) * 2+(num_elements_difference - 1) * 2 * num_equal_elements
    return  max_diff


def main():
    t=int(input())

    for  _ in  range(0, t):
        n, m=map(int, input().split())
        print(max_difference_array(n, m))


if  __name__=="__main__":
    main()