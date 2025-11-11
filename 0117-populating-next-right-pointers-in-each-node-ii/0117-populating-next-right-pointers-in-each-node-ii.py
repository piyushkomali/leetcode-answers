"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        q = []
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                pop = q.pop(0)
                
                if pop.left: q.append(pop.left) 
                if pop.right: q.append(pop.right) 
            
            if q: 
                assign = q[0]
                for a in q:
                    assign.next = a
                    assign = a
                assign.next = None 
        return root
#1
#2,3