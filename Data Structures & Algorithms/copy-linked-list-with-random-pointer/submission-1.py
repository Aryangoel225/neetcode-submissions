"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}  # hashmap to store original node -> copied node mappings

        # First loop: create all node copies and store them in the hashmap
        curr = head
        while curr:
            copy = Node(curr.val)  # create a copy of the current node
            oldToCopy[curr] = copy  # map original node to its copy
            curr = curr.next 
        
        # Second loop: assign next and random pointers for each copied node
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
        