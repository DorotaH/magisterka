base = 998244353;


def power(x, y):
	if (y == 0):
		return 1
	t = power(x, y // 2)
	t = (t * t) % base
	if (y % 2):
		t = (t * x) % base
	return t;


def inverse(x):
	return power(x, base - 2)


f = [1]
iv = [1]
for i in range(1, 5555):
	f.append((i * f[i - 1]) % base)
	iv.append(inverse(f[i]))


def C(n, k):
	return (f[n] * iv[k] * iv[n - k]) % base


def candy(n, k):
	# print(n, k)
	return C(k + n - 1, k - 1)


def count_game(k, n, x): #k players, n points total, no player can have x point or more
	if (k == 0):
		return 1 if (n == 0) else 0
	ans = 0
	for i in range(0, k + 1):
		t = n - i * x
		# print(i, C(k, i))
		if (t < 0):
			break
		if (i % 2):
			ans = (ans - C(k, i) * candy(t, k)) % base
		else:
			ans = (ans + C(k, i) * candy(t, k)) % base
	return ans


p, s, r = list(map(int, input().split()))
gamesize = count_game(p, s - r, int(1e18))
gamesize = inverse(gamesize)
ans = 0;
for q in range(r, 1 + s):
	for i in range(0, p): #exactly i people have the same score
		t = s - (i + 1) * q
		if (t < 0):
			break
		# print(q, i, count_game(p-i-1, t, q));
		ans = (ans + count_game(p - i - 1, t, q) * C(p - 1, i) * gamesize * inverse(i + 1)) % base
print(ans)
		
