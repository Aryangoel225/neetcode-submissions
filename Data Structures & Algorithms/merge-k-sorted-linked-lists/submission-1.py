# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the list is empty, return None
        if not lists or len(lists) == 0:
            return None
        
        # Keep merging until there is only one list left
        while len(lists) > 1:
            mergedLists = []  # This will store the merged lists after each round

            # Merge two lists at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # First list
                # Second list (if exists), otherwise None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None 
                
                # Merge l1 and l2 and add the result to mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            
            # Update lists to the newly merged lists
            lists = mergedLists
        
        # Finally, return the only list left
        return lists[0]

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to help build the result list
        tail = dummy        # Tail pointer to track the end of the merged list
        
        # While both lists are not empty
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # Attach l1 to the result
                l1 = l1.next    # Move l1 forward
            else:
                tail.next = l2  # Attach l2 to the result
                l2 = l2.next    # Move l2 forward
            tail = tail.next    # Move the tail forward
        
        # If any list still has nodes left, attach it
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        # Return the merged list, starting from dummy.next
        return dummy.next