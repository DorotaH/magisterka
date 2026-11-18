#! /usr/bin/env python

# http://codeforces.com/problemset/problem/818/F
# Problem name ::: F. Level Generation
# submission number

#212055293
#508427854


def newest_approach(n):
    from math import ceil, floor, sqrt

    quad_solv = sqrt(2*n + 1/4) - 1/2
    x, y = floor(quad_solv), ceil(quad_solv)

    xed, xbr = int(x*(x-1)/2 + n - x), n - x

    ybr = n - y
    yed = ybr*2

    if not xed > yed:
        print(yed)
        # print("nodes = %s :: edges = %s :: bridges = %s" % (n, yed, ybr))
    else:
        print(xed)
        # print("nodes = %s :: edges = %s :: bridges = %s" % (n, xed, xbr))




def main():

    import sys

    data = [line.rstrip() for line in sys.stdin.readlines()]
    num_graphs, graph_sizes = data[0], [int(x) for x in data[1:]]

    for  val in  graph_sizes:
        # binary_search(val)
        # new_approach(val)
        newest_approach(val)





def __starting_point():
    main()

__starting_point()