# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative bfs appoarch compare each value at each turn
        def bfs(start1, start2):
            q1 = deque([start1])
            q2 = deque([start2])

            while q1 or q2:
                node1 = q1.popleft()
                node2 = q2.popleft()

                if node1.val != node2.val:
                    return False
                # process node
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

        if not p and q:
            return False
        if not q and p:
            return False
        if not q and not p:
            return True
        return bfs(p, q)

        