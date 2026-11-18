n = int(input())
out = []
def  p(a,b,d):
    out.append(str(1 + a+d)+' '+str(1+b+d))

p2=1
while  p2 * 2 <= n:
    p2 *= 2

for  d in  (0, n - p2):
    bit=1
    while  p2 > bit:
        for i in range(0, p2):
            if  i^bit>i:
                p(i, i^bit, d)
        bit = bit * 2
print(len(out))
print('\n'.join(out))
