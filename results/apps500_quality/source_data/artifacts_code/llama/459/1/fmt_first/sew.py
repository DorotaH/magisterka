import sys


def  check_cube(s):
    colors = [0, 0, 0, 0]
    for  i in  range(24):
        colors[s[i]-1]+=1

    # Check if all colors have the same count
    for  c in  colors:
        if  4 != c:
            return "NO"

    # Check if each face has the same color
    for  i in  range(0, 6, 4):
        face_colors=sorted(s[i : i + 4])
        if  (
            face_colors!=[1, 1, 1, 1]
            and  face_colors!=[2, 2, 2, 2]
            and  face_colors!=[3, 3, 3, 3]
            and  face_colors!=[4, 4, 4, 4]
            and  face_colors!=[5, 5, 5, 5]
            and  face_colors!=[6, 6, 6, 6]
            ):
            return "NO"

    # Check if it's possible to rotate to a solved state
    for  i in  range(6):
        if  (
            s[i] == s[i + 4]
            and  s[i + 8] == s[i + 12]
            and  s[i + 20] == s[i + 16]
            and  s[i] == s[i + 24]
            ):
            return "YES"

    return  "NO"


# Read input from standard input
input_str=sys.stdin.readline().strip()
s=list(map(int, input_str.split()))

print(check_cube(s))
