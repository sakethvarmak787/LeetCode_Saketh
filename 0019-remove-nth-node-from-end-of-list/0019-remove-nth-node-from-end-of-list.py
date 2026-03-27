class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # move both until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # delete the nth node from end
        slow.next = slow.next.next
        
        return dummy.next