import  sys
from  typing import  List, Tuple

def read_input() -> Tuple[int, List[Tuple[int, int]], Tuple[int, int]]:
    input=sys.stdin.read
    data=input().split()
    
    n=int(data[0])
    x1 = int(data[1])
    y1 = int(data[2])
    x2 = int(data[3])
    y2 = int(data[4])
    
    flowers=list()
    for  i in  range(n):
        x, y = int(data[5 + 2 * i]), int(data[6 + 2 * i])
        flowers.append((x, y))
    
    return  (n, flowers, (x1, y1, x2, y2))

def distance(p1, p2):
    return  ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def find_min_r2(n, flowers, f1, f2):
    min_r2=float('inf')
    for  flower in  flowers:
        d1, d2 = distance(flower, f1), distance(flower, f2)
        min_r2=min(min_r2, max(d1, d2))
    return  min_r2

def main():
    n, flowers, (x1, y1, x2, y2)=read_input()
    
    min_r1 = 0
    min_r2 = find_min_r2(n, flowers, (x1, y1), (x2, y2))
    
    print(int(pow(min_r1, 2)+pow(min_r2, 2)))

if  __name__=="__main__":
    main()