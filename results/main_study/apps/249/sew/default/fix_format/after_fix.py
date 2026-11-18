

def  can_measure(a, d):
	for i in a:
		if i + d in a:
			return True
	return False


def  main():
	n, l, x, y=list(map(int, input().split()))
	a=set(map(int, input().split()))
	
	can_x, can_y = can_measure(a, x), can_measure(a, y)
	if  can_x and  can_y:
		print(0)
	elif  can_x:
		print(1)
		print(y)
	elif  can_y:
		print(1)
		print(x)
	else:
		for  i in  a:
			if not i + x + y in a:
				t = i + x - y in a
				if 0 <= i + x <= l and t:
					print(1)
					print(i + x)
					break;
				if 0 <= i - y <= l and t:
					print(1)
					print(i - y)
					break;
			else:
				print(1)
				print(i + x)
				break
				
		else:
			print(2)
			print(x, y)
		

def  __starting_point():
	main()

__starting_point()