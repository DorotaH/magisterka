def count_subpermutations(n, a):
	count = 0
	left = 0
	seen = [0] * (1 + n)
	for right in range(n):
		seen[a[right]] += 1
		while all(seen[i] > 0 for i in range(1, right - left + 2)):
			count += n - right
			seen[a[left]] -= 1
			left += 1
	return count


# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(count_subpermutations(n, a))
