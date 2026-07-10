# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # divide the list in half by using a slow and fast pointer
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # cut the first list off
        second = slow.next
        slow.next = None   

        prev = None
        while second != None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        p2 = prev
        p1 = head


        # merge the two list alternatinve 
        while p1 != None and p2 != None:
            p1nxt = p1.next
            p2nxt = p2.next
            p1.next = p2
            p2.next = p1nxt
            p1 = p1nxt
            p2 = p2nxt


        

