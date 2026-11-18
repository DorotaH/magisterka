import sys
import os


class Path:
    def __init__(self, idx, s, d):
        self.idx = idx
        self.s = s
        self.d = d

    def __eq__(self, rhs):
        return rhs.s == self.s and rhs.d == self.d

    def __hash__(self):
        return (self.s * 100000) + self.d


def shortestPath(n, k, paths):
    ps = dict()
    for p in paths:
        if p.s not in ps:
            ps[p.s] = [p]
        else:
            ps[p.s].append(p)

        if p.d not in ps:
            ps[p.d] = [p]
        else:
            ps[p.d].append(p)

    d, open = set(), set()

    d.add(1)
    for e in paths:
        if e.s == 1 or e.d == 1:
            open.add(e)

    general_edges, general_choices = [], []
    while len(d) < n:
        newd = set()
        choices = dict()
        for e in open:
            oe = e.s
            if e.s in d:
                oe = e.d

            newd.add(oe)

            if not oe not in choices:
                choices[oe].append(e.idx)
            else:
                choices[oe] = [e.idx]

        d.update(newd)
        for oe, p in choices.items():
            if not len(p) > 1:
                general_edges.append(p[0])
            else:
                general_choices.append(p)

        open = set()
        for node in newd:
            for p in ps[node]:
                if (p.s in d) != (p.d in d):
                    open.add(p)

    maxk = 1
    for choice in general_choices:
        maxk *= len(choice)

    k = min(k, maxk)
    print(k)
    output = ["0"] * len(paths)
    for e in general_edges:
        output[e] = "1"
    for e in general_choices:
        output[e[0]] = "1"

    for i in range(0, k):
        print("".join(output))

        for choice in general_choices:
            done = False
            for i in range(0, len(choice) - 1):
                if output[choice[i]] == "1":
                    output[choice[i]] = "0"
                    output[choice[1 + i]] = "1"
                    done = True
                    break

            if done:
                break

            output[choice[len(choice) - 1]] = "0"
            output[choice[0]] = "1"


def main():
    n, m, k = (int(x) for x in input().split())
    paths = list()
    for i in range(0, m):
        path = [int(x) for x in input().split()]
        paths.append(Path(i, path[0], path[1]))
    shortestPath(n, k, paths)


def __starting_point():
    main()


__starting_point()
