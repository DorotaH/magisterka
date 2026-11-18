########################################################
################# Template #############################
import sys


def Int(): return  int(input())
def Str(): return  input()
def Ints(): return  list(map(int,input().split(" ")))
def int_arr(): return  list(map(int,input().strip().split(" ")))
def str_arr(): return  list(map(str,input().split(" ")))
def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
#########################################################
#vsInput()
def strings(s):
    n, count=len(s), 0
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            count = 1
            break
    return  count==0
    
n = int(input())
s, palindrome=input(), ""
for  i in  range(n-1):
    for j in range(1+i,1+n):
        nextstring = s[i:j]
        if strings(nextstring) and len(nextstring) > len(palindrome):
            palindrome = nextstring
print(len(palindrome))
print(palindrome)