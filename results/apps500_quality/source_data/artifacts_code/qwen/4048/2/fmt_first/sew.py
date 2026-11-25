import  sys

input = sys.stdin.read
data = input().split()

N = int(data[0])


# Function to calculate the minimum number of moves to reach a square that contains N
def  min_moves(N):
    # The minimum number of moves to reach a square that contains N is the sum of the digits of N in base 10
    return  sum(int(digit) for  digit in  str(N))


# Output the result
print(min_moves(N))
