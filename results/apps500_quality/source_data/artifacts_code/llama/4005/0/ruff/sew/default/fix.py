
x1, y1, x2, y2=map(int, input().split())
x3, y3, x4, y4=map(int, input().split())
x5, y5, x6, y6=map(int, input().split())

def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return  False

def do_intersect(r1, r2):
    x1, y1, x2, y2=r1
    x3, y3, x4, y4=r2
    return  not  (max(x1, x2) < min(x3, x4) or
                max(x3, x4) < min(x1, x2) or
                max(y1, y2) < min(y3, y4) or
                max(y3, y4) < min(y1, y2) or
                on_segment((x1, y1), (x3, y3), (x4, y4)) or
                on_segment((x1, y1), (x4, y4), (x3, y3)) or
                on_segment((x2, y2), (x3, y3), (x4, y4)) or
                on_segment((x2, y2), (x4, y4), (x3, y3)))

if not (not do_intersect((x1, y1, x2, y2), (x3, y3, x4, y4)) and not do_intersect((x1, y1, x2, y2), (x5, y5, x6, y6))):
    print("NO")
else:
    print("YES")