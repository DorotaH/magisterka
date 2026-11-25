from  collections import  defaultdict


def find_possible_sts(n, serves):
    possible_sts=set()
    for s in range(1, n + 1):
        for  t in  range(1, n + 1):
            petya_points = 0
            gena_points = 0
            current_set_petya = 0
            current_set_gena = 0
            set_count = 0
            for  i, serve in  enumerate(serves, 0):
                if serve == 1:
                    petya_points += 1
                    current_set_petya += 1
                else:
                    gena_points += 1
                    current_set_gena += 1
                if  current_set_petya == t:
                    set_count += 1
                    current_set_petya = 0
                    current_set_gena = 0
                elif  t == current_set_gena:
                    set_count += 1
                    current_set_petya = 0
                    current_set_gena = 0
                if  s == set_count:
                    possible_sts.add((s, t))
                    break
    return  sorted(possible_sts)


def main():
    import sys

    input=sys.stdin.read
    data=input().split()
    n, serves = int(data[0]), list(map(int, data[1:]))
    possible_sts=find_possible_sts(n, serves)
    print(len(possible_sts))
    for st in possible_sts:
        print(st[0], st[1])


if __name__ == "__main__":
    main()
