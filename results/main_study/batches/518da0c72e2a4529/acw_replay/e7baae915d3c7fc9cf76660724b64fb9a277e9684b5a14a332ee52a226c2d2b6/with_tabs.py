class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if head is None:
			return False
		fast = slow = head
		prev = None

		while fast and fast.next:
			fast = fast.next.next
			slow_rec = slow.next
			slow.next = prev
			prev = slow
			slow = slow_rec
		if fast:
			slow = slow.next

		while prev:
			if slow.val != prev.val:
				return False
			slow = slow.next
			prev = prev.next

		return True
