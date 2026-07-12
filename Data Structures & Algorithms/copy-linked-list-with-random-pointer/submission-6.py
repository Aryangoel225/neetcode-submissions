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
        if head is None:
            return None
        # create a hashmap copy for old to new 
        oldToCopy = {} 
        # walk through the orginal list map each old to a new copy
        # only copy the val, bc pointer would still point to old list
        curr = head
        while curr != None:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        # walk through all of the keys of the hashmap
        # get each copied object and set next and random equal to the new copy obj or None
        for key in oldToCopy:
            oldToCopy[key].next = oldToCopy[key.next] if key.next else None
            oldToCopy[key].random = oldToCopy[key.random] if key.random else None

        return oldToCopy[head]
        