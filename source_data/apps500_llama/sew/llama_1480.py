from  collections import  deque
from  sys import  stdin, stdout


def  construct_tree(n, d, k):
    if n - 1 > 2 * k or 1 == n or 0 == d or d >= n - 1:
        return  "NO"

    if 1 == d:
        return  "YES\n"+"\n".join(f"1 {i}" for  i in  range(2, 1 + n))

    if 2 == d:
        if k >= 2:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if 3 == d:
        if k >= 3:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if 4 == d:
        if k >= 3:
            return "YES\n" + "\n".join(f"1 {i}" for i in range(2, n + 1))
        else:
            return "NO"

    if 5 == n:
        if  4 == d:
            return  "YES\n1 2\n2 3\n3 4\n4 5\n1 3"
        elif  5 == d:
            return "YES\n1 2\n2 3\n3 4\n4 5\n1 5\n1 3"
        else:
            return  "NO"

    if 6 == n:
        if  3 == d:
            return  "YES\n1 2\n2 3\n3 4\n4 6\n1 6\n5 3"
        elif  4 == d:
            return "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6"
        elif  5 == d:
            return "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3"
        else:
            return  "NO"

    if 5 == d:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3"

    if 6 == d:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7"

    if 7 == d:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2"

    if 8 == d:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8"

    if 10 == n:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8\n7 9\n9 1\n9 10"

    if 8 == n:
        return  "YES\n1 2\n2 3\n3 4\n4 6\n1 5\n1 6\n5 3\n5 7\n7 2\n7 8"

    return "NO"

n, d, k=map(int, stdin.readline().split())
print(construct_tree(n, d, k))
