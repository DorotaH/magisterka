# Przykłady i ścieżka dowodowa

Wybór przykładów jest deterministyczny. Pełne bajty kodu są w SQLite; poniższy tekst służy tylko do czytania.

## Uszkodzenie wcięcia: zadanie 2

### Przed regułą 45

````python
def similar_elements(test_tup1, test_tup2):
  return tuple(set(test_tup1) & set(test_tup2))

````

### Po regule 45

````python
def similar_elements(test_tup1, test_tup2):
return tuple(set(test_tup1) & set(test_tup2))

````

## Największa bezwzględna zmiana złożoności funkcji: acw, ID 306

Przed: 17.0; po: 11.0; delta: -6.0. To wybrany skrajny przykład, nie reprezentatywna średnia.

### original

````python
def max_sum_increasing_subseq(a, n, index, k):
	dp = [[0 for i in range(n)] 
			for i in range(n)]
	for i in range(n):
		if a[i] > a[0]:
			dp[0][i] = a[i] + a[0]
		else:
			dp[0][i] = a[i]
	for i in range(1, n):
		for j in range(n):
			if a[j] > a[i] and j > i:
				if dp[i - 1][i] + a[j] > dp[i - 1][j]:
					dp[i][j] = dp[i - 1][i] + a[j]
				else:
					dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[index][k]
````

### acw

````python
def max_sum_increasing_subseq(a, n, index, k):
	dp = [[0 for i in range(n)] 
			for i in range(n)]
	for i in range(n):
		dp[0][i] = a[0] + a[i] if a[0] < a[i] else a[i]
	for i in range(1, n):
		for j in range(n):
			if a[j] > a[i] and i < j:
				dp[i][j] = max(a[j] + dp[i - 1][i], dp[i - 1][j])
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[index][k]

````

## Największa bezwzględna zmiana złożoności funkcji: sew, ID 200

Przed: 0.0; po: 3.0; delta: 3.0. To wybrany skrajny przykład, nie reprezentatywna średnia.

### original

````python
def position_max(list1):
    max_val = max(list1)
    max_result = [i for i, j in enumerate(list1) if j == max_val]
    return max_result
````

### sew

````python
def  position_max(list1):
    max_val=max(list1)
    max_result = []
    for i, j in enumerate(list1):
        if j == max_val:
            max_result.append(i)
    return  max_result

````

