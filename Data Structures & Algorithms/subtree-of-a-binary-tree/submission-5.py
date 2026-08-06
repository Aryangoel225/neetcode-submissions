# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = deque([root1])
        q2 = deque([root2])

        while q1:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1.val != node2.val:
                return False

            if node1.left or node2.left:
                if node1.left:
                    q1.append(node1.left)
                else:
                    return False
                if node2.left:
                    q2.append(node2.left)
                else:
                    return False

            if node1.right or node2.right:
                if node1.right:
                    q1.append(node1.right)
                else:
                    return False
                if node2.right:
                    q2.append(node2.right)
                else:
                    return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return False
            if self.sameTree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)



          
        
        