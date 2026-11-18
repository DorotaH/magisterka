# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class  Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listi = list()
        while head!=None:
            listi.append(head.val)
            head = head.next
        for  i in  range(0, len(listi)):
            temp = listi[i] #2
            red = i - 1 #0
            while(red >= 0 and temp < listi[red]):
                listi[red+1] = listi[red]
                red=red-1
            listi[red+1] = temp
        cur = head = ListNode(0)
        for  i in  listi:
            cur.next = ListNode(i)
            cur = cur.next
        return  head.next


