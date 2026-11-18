# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_l = []
        if head is None:
            return(None)
        while head is not None:
            if(head.val not in current_l):
                current_l.append(head.val)
            else:
                head = head.next

        current = ListNode()
        current_l.reverse()
        flag = 0
        while flag < len(current_l):
            if flag == 0:
                current = ListNode(current_l[flag])
            else:
                current = ListNode(current_l[flag], next = current)
            flag += 1

        return current