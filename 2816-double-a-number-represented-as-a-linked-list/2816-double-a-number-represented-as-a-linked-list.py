# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        curr = head
        if head.next == None and head.val == 0:
            return head
        while(curr):
            res = res * 10 + curr.val
            curr = curr.next
        
        number = res*2

        head = ListNode(0)
        curr = head
        while number > 0:
            
            curr.next = ListNode(number%10)
            number //= 10
            curr = curr.next
            
        prev = None
        temp = None
        curr = head.next
        
        while(curr):
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            
            
        return prev