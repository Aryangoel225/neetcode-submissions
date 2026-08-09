# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breath first search on a binary tree
        res = []
        # iterative appoarch 
        def bfs(root, res):
            if not root:
                return []
            q = deque()
            q.append(root)
            
            while q:
                n = len(q)          # size of current level, captured before mutating
                level = []
                for _ in range(n): # pop for current val and then 
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level)
            return res
        return bfs(root, res)


                    
                    
                
            

        