import sys
input = sys.stdin.read
data = input().split()

R = int(data[0])
G = int(data[1])

# The performance required to achieve the desired rating
performance = 2 * G - R

print(performance)
