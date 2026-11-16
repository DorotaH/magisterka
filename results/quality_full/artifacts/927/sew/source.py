class  Node: 
	def  __init__(self, data): 
		self.data=data 
		self.left=None
		self.right=None
def  max_height(node): 
	if not node is None: 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1 
	else : 
		return 0 ;
