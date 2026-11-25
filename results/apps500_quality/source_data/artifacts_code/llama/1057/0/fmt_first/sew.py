import  sys

input=sys.stdin.readline

def prod(a, mod):
    ans=1
    for  x in  a:
        ans = (x * ans) % mod
    return  ans

class  Mint:
    def __init__(self, x, mod):
        self.x=x%mod
        self.mod=mod
    def __add__(self, other):
        if not isinstance(other, Mint):
            return Mint(self.x + other, self.mod)
        else:
            return Mint(self.x + other.x, self.mod)
    def __sub__(self, other):
        if not isinstance(other, Mint):
            return Mint(self.x - other, self.mod)
        else:
            return Mint(self.x - other.x + self.mod, self.mod)
    def __mul__(self, other):
        if not isinstance(other, Mint):
            return Mint(self.x * other, self.mod)
        else:
            return Mint((self.x * other.x) % self.mod, self.mod)
    def __truediv__(self, other):
        if not isinstance(other, Mint):
            return Mint(self.x // other, self.mod)
        else:
            return Mint(
                (self.x * pow(other.x, self.mod - 2, self.mod)) % self.mod, self.mod
            )
    def __pow__(self, other):
        if not isinstance(other, Mint):
            return Mint(pow(self.x, other, self.mod))
        else:
            return Mint(pow(self.x, other.x, self.mod), self.mod)
    def __eq__(self, other):
        if not isinstance(other, Mint):
            return self.x == other
        else:
            return self.x == other.x
    def __ne__(self, other):
        if not isinstance(other, Mint):
            return self.x != other
        else:
            return self.x != other.x
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return str(self)
    def inv(self):
        return pow(self, (self.mod - 2))
    def __iadd__(self, other):
        if not isinstance(other, Mint):
            self.x = (self.x + other) % self.mod
        else:
            self.x = (self.x + other.x) % self.mod
        return self
    def __isub__(self, other):
        if not isinstance(other, Mint):
            self.x = (self.x - other + self.mod) % self.mod
        else:
            self.x = (self.x - other.x + self.mod) % self.mod
        return self
    def __imul__(self, other):
        if not isinstance(other, Mint):
            self.x = (self.x * other) % self.mod
        else:
            self.x = (self.x * other.x) % self.mod
        return self
    def __itruediv__(self, other):
        if not isinstance(other, Mint):
            self.x = (self.x // other) % self.mod
        else:
            self.x = (self.x * other.inv()) % self.mod
        return self
    def __ipow__(self, other):
        if not isinstance(other, Mint):
            self.x = pow(self.x, other, self.mod)
        else:
            self.x = pow(self.x, other.x, self.mod)
        return self

def count(a):
    n=len(a)
    left, right = [0] * (n + 1), [0] * (n + 1)
    for  i in  range(1, n + 1):
        left[i] = left[i - 1]
        if a[0] == a[i - 1]:
            left[i]+=1
    for  i in  reversed(range(n)):
        right[i] = right[1 + i]
        if a[-1] == a[i]:
            right[i]+=1
    cnt=0
    for  i in  range(n):
        for  j in  range(1 + i, n):
            if a[j] == a[i]:
                cnt += 1
    if  n == cnt:
        return Mint(0, 998244353)
    ans=0
    for  i in  range(1, n):
        if a[0] != a[i - 1]:
            ans += (left[i - 1] * right[i]) % 998244353
    for  i in  range(n - 1):
        if a[-1] != a[i]:
            ans += (left[i] * right[i + 1]) % 998244353
    ans *= 2
    for  i in  range(1, n):
        if a[0] != a[i - 1] and a[-1] != a[i]:
            ans -= (left[i - 1] * right[i]) % 998244353
    for  i in  range(n - 1):
        if a[-1] != a[i] and a[0] != a[i + 1]:
            ans -= (left[i] * right[i + 1]) % 998244353
    ans += 1
    return  ans


n = int(input())
s = input().strip()
print(count(s))
