#86 Partition List
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after
        
        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next
        
        after_curr.next = None
        before_curr.next = after.next
        
        return before.next


from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = SortedList()
        l.update(nums[0:k])
        print(nums[0:k])
        ans = [l[-1]]
        for i in range(k,len(nums)):
            l.remove(nums[i-k])
            l.add(nums[i])
            #print(l)
            ans.append(l[-1])

        return ans
