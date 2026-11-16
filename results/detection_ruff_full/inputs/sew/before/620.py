def largest_subset(a, n):
	dp=[0 for i in range(0, n)]
	dp[n-1]=1; 
	for i in range(n - 2, -1, -1):
		mxm=0;
		for j in range(i + 1, n):
			if 0 == a[j] % a[i] or 0 == a[i] % a[j]:
				mxm = max(mxm, dp[j])
		dp[i]=1 + mxm
	return  max(dp)