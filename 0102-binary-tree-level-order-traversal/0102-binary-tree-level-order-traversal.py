# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[]]
        if not root: return []
        def dfs(root, level=1):
            if not root: return
            if len(res) < level:
                res.append([root.val])
            else: res[level-1].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,1)
        return res
        