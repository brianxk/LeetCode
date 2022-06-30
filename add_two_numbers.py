# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""
        
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
            
        s1 = int(s1[::-1])
        s2 = int(s2[::-1])
        
        total = str(s1 + s2)[::-1]
        
        result = ListNode()
        next_node = result
        
        for c, i in enumerate(total):
            next_node.val = int(i)
            
            if c < len(total) - 1:
                next_node.next = ListNode()
                next_node = next_node.next
        
        return result