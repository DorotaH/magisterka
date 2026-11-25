import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = []
K = []
for i in range(N):
    A.append(int(data[2*i+1]))
    K.append(int(data[2*i+2]))

# The game can be reduced to a Nim game where each pile has a size of A_i % K_i
# The player who faces a position with all piles of size 0 loses
# This is because they will be the one to face a position where they cannot make a move
# We can use the Nim-sum (XOR of all pile sizes) to determine the winner
# If the Nim-sum is 0, the player who is about to move loses
# If the Nim-sum is non-zero, the player who is about to move wins

nim_sum = 0
for i in range(N):
    nim_sum ^= A[i] % K[i]

if nim_sum == 0:
    print("Aoki")
else:
    print("Takahashi")
