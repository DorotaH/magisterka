#	!/usr/bin/env python3
#	coding: UTF-8
#	Modified: <23/Jan/2019 08:06:42 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT),Gwalior

#	Question Link
#
#

# ///==========Libraries, Constants and Functions=============///


import  sys

inf, mod = float("inf"), 1000000007

def  get_array(): return list(map(int, sys.stdin.readline().split()))

def  get_ints(): return list(map(int, sys.stdin.readline().split()))

def  input(): return sys.stdin.readline()

# ///==========MAIN=============///


def  main():
    for  tc in  range(0, int(input())):
        l1, r1, l2, r2 = get_ints()
        if not l1 != l2:
            print(l1, r2)
        else:
            print(l1, l2)

def  __starting_point():
    main()

__starting_point()