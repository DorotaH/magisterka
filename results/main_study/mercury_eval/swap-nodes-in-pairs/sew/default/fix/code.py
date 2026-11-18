# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class  Solution:
    def  swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  head is  None or  head.next is  None:
            return  head
        prev, slow = ListNode(0), head
        fast = head = head.next
        
        while 1:
            prev.next = fast
            slow.next = fast.next
            fast.next = slow

            prev = slow
            slow = slow.next
            if slow is None:
                return  head

            fast = slow.next
            if fast is None:
                return  head