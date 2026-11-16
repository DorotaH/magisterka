def lbs(arr): 
	n=len(arr) 
	lis=[1 for i in range(n+1)] 
	for  i in  range(1 , n): 
		for j in range(i): 
			if  ((arr[j] < arr[i]) and  (lis[i]<lis[j] +1)): 
				lis[i] = lis[j] + 1
	lds=[1 for i in range(n+1)] 
	for  i in  reversed(range(n-1)): 
		for j in reversed(range(i-1 ,n)): 
			if(arr[j] < arr[i] and  lds[i]<lds[j] + 1): 
				lds[i] = lds[j] + 1
	maximum=lis[0]+lds[0]-1
	for  i in  range(1 , n): 
		maximum=max((lis[i]+lds[i]-1), maximum) 
	return  maximum