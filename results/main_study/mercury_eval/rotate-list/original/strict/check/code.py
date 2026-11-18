# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # length = self.getLength(head)
        # k = 0 if length == 0 else k % length
        # if head == None or k == 0: return head

        # tempHead = head
        # for _ in range(length - k - 1):
        #     head =  head.next

        # if head.next:
        #     curr = head.next
        #     head.next = None
        #     head = curr
        # curr = head
        # while curr.next:
        #     curr = curr.next
        # curr.next = tempHead
        
        # return head

        if head == None or head.next == None:
            return head
        
        consst = head

        curr = head
        size = 1
        while curr.next != None:
            curr = curr.next
            size += 1

        k = k % size
        
        if k == 0:
            return head
        
        iterator = size - k
        new_curr = head
        while (iterator > 1):
            new_curr = new_curr.next
            iterator -= 1
        head = new_curr.next
        new_curr.next = None
        curr.next = consst
        
        
        return head

    def getLength(self, node: ListNode) -> int:
        length = 0
        while node:
            length += 1
            node = node.next
        return length
        