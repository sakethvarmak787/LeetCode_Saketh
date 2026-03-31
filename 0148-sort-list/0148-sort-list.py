class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # STEP 1: find middle
        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # cut the list into two halves
        prev.next = None
        
        # STEP 2: sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # STEP 3: merge
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        # attach remaining
        tail.next = l1 if l1 else l2
        
        return dummy.next