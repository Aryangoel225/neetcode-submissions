# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs search to build an array
        # sort the array
        # return the index k - 1
        # the appoarch above the is the naive solution

        # better solution is dfs and then do a in-order-traversal 

        stack = []
        current = root
        count = 0
        
        while current is not None or len(stack) > 0:
            # Reach the leftmost node of the current node
            while current is not None:
                stack.append(current)
                current = current.left
            
            # Current must be None at this point
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            
            # now right subtree
            current = current.right
                
        
                        

