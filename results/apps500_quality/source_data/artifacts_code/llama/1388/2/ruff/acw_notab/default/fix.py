

class FastIO:
    def __init__(self):
        import sys
        self.input = sys.stdin
        self.output = sys.stdout
        self.buffer = ''
        self.buffering = True

    def input(self):
        return self.input.readline().strip() if self.buffering else input()

    def flush(self):
        if self.buffering:
            self.buffering = False

    def output(self, s):
        self.output.write('\n' + str(s))

    def flush_output(self):
        self.output.flush()

    def reset(self):
        self.buffering = True
        self.buffer = ''

    def seek_input(self):
        self.buffering = True
        self.buffer = self.input().strip()
        self.buffering = False

    def readline(self):
        if not self.buffer:
            return self.input()
        line, self.buffer = self.buffer.split('\n'), ''
        return line

    def next_int(self):
        return int(self.readline())

    def next_ints(self, n):
        return list(map(int, self.readline().split(' ')))

    def next_long(self):
        return int(self.readline())

    def next_longs(self, n):
        return list(map(int, self.readline().split(' ')))

    def next_double(self):
        return float(self.readline())

    def next_doubles(self, n):
        return list(map(float, self.readline().split(' ')))

    def next_chars(self):
        return list(self.readline())

    def next_string(self):
        return self.readline()

    def next_strings(self, n):
        return self.readline().split(' ')


io = FastIO()

n = io.next_int()

adj = [[] for _ in range(n)]
cost = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    cost[i], b[i], c[i] = io.next_ints(3)

for i in range(n - 1):
    u, v = io.next_ints(2)
    u, v = u - 1, v - 1
    adj[u].append(v)
    adj[v].append(u)

dp = [0] * n
stack = [0]
dp[0] = cost[0]

for i in range(n):
    while len(stack) > 0 and c[stack[-1]] != c[i]:
        u = stack.pop()
        for v in adj[u]:
            if v != stack[-1]:
                adj[v].remove(u)
    if len(stack) == 0 or c[stack[-1]] != b[i]:
        cost[i] = 0
        stack.append(i)
        dp[i] = cost[i]
    else:
        u = stack[-1]
        for k in range(1, 1 + len(adj[u])):
            v = u
            while len(stack) > 0 and c[stack[-1]] == c[v]:
                v = stack.pop()
                k += 1
            if len(stack) > 0 and c[stack[-1]] == b[v]:
                dp[u] = max(dp[u], dp[v] + (cost[u] * k))
            else:
                dp[u] = max(dp[u], cost[u] * k)

ans = sum(dp)

for i in range(1, n):
    ans = max(ans, cost[i] * len(adj[i]) + dp[i])

if ans == -1:
    io.output(-1)
else:
    io.output(ans)
io.flush_output()
