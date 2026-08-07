# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # bfs appoarch recursive
        # binary tree, need to track the most recent lowest value int
        # if p and q are in different subtree then make the current node LCA and return
        # if they are in thesame subtree keep recursing

        def dfs(root):
            # Base Case: stop when there are no more nodes to process
            if not root:
                return
            
            if p.val > root.val and q.val > root.val:
                return dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                return dfs(root.left)
            else:
                return root
    
        return dfs(root)


