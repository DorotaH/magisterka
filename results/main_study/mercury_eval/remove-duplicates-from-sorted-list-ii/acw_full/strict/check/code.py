# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head is None:
			return head
		arr = []
		while head is not None:
			arr.append(head.val)
			head = head.next
		arr = [i for i in arr if arr.count(i) == 1]
		print(arr)
		if not arr:
			return None
		node = ListNode(arr[0])
		newnode = node
		for i in range(1, len(arr)):
			node.next = ListNode(arr[i])
			node = node.next
		return newnode
