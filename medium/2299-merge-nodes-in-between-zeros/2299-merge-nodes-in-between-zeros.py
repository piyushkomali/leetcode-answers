# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, rHead, curr = 0, ListNode(), head.next
        rCurr = rHead
        while (curr):
            if curr.val == 0:    
                rCurr.val = s
                if curr.next: rCurr.next = ListNode()
                rCurr = rCurr.next
                s = 0
            else:
                s += curr.val
            curr = curr.next
        return rHead

        