# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def splitList(self, head: ListNode) -> List[Optional[ListNode]]:
        if not head.next:
            return [None, head, None]
        
        half_length = self.getLength(head) // 2
        prev_node, cur_node = None, head
        for _ in range(half_length):
            prev_node, cur_node = cur_node, cur_node.next
        
        prev_node.next = None
        head2 = cur_node.next 
        cur_node.next = None
        return head, cur_node, head2


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        head1, root, head2 = self.splitList(head)

        root.left = self.sortedListToBST(head1)
        root.right = self.sortedListToBST(head2)

        return root
