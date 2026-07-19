# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy list
        dummy = ListNode()
        carry = 0
        # curr pointer to dummy
        curr = dummy
        # create a while loop based on the length of the long list + carry = null
        while l1 != None or l2 != None or carry != 0:
            # each node add the value of each node (if val is null = 0) + carry and create an new node for res list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = carry + val1 + val2   
            # if sum is >= 10 use the sum % 10 for the node
            # use sum // 10 as carry value
        
            carry = s // 10 
            s = s % 10
            curr.next = ListNode(s, None)
            curr = curr.next
            if l1:
                l1 =l1.next
            if l2:
                l2 = l2.next

        return dummy.next

        