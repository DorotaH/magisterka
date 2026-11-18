# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not (len(lists)):
            return None
        else:
            output = lists[0]
            for i in range(1, len(lists)):
                temp1 = lists[i]
                temp2 = output
                prev = None
                while temp2 and temp1:
                    if temp1.val < temp2.val:
                        if prev:
                            prev.next = temp1
                            temp = temp1.next
                            temp1.next = temp2
                            temp1 = temp
                            prev = prev.next
                        else:
                            temp = temp1.next
                            temp1.next = temp2
                            output = temp1
                            temp1 = temp
                            prev = output
                    else:
                        prev = temp2
                        temp2 = temp2.next
                if temp1:
                    if prev:
                        prev.next = temp1
                    else:
                        output = temp1

            return output
