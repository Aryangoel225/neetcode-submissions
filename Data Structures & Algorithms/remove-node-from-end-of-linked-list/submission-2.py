# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        fast = head
        for i in range(n):
            fast = fast.next
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        
        # have a pointer n + 1 length away another fast pointer
        # then when fast pointer reach end, n.next.next
        # edge case what if the list isn't long enough return None
        # what if its the head to remove then move one down from head and return 
        