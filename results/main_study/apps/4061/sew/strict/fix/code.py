import sys

input = sys.stdin.readline
s = input()
t = input()
l = [0]*len(t)
r = [0]*len(t)
li = 0
ri = len(s) - 1
for  i in  range(0, len(t)):
    while t[ i ] != s[ li ]:
        li += 1
    while t[ - i - 1 ] != s[ ri ]:
        ri -= 1
    l[ i ]=li
    r[ -i -1 ]=ri
    li += 1
    ri -= 1

print( max( [ r[ 0 ], len(s) - l[ -1 ] - 1 ] + [ max( 0, r[ i ] - l[ i - 1 ] ) - 1 for  i in  range( 1, len(t) ) ] ) )
