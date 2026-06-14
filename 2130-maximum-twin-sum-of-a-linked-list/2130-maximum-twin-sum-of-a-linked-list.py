class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next

        
        max_sum = 0
        current = head
        while stack:
            max_sum = max(max_sum, current.val + stack.pop())
            current = current.next

        return max_sum
