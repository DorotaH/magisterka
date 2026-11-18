#!/usr/bin/env python3


def main():

    class Node:
        def __init__(self):
            self.children = []

    n = int(input())
    nodes = [Node() for _ in range(n)]
    for i in range(1, n):
        p = int(input())
        nodes[p - 1].children.append(nodes[i])
    ok = all(
        3 <= len([child for child in node.children if not child.children])
        for node in nodes
        if node.children
    )
    print("Yes" if ok else "No")


try:
    while True:
        main()
except EOFError:
    pass
