class Solution:
    def partition(self, head, x):
        # two dummy lists
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        curr = head
        
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            
            curr = curr.next
        
        # important: end greater list
        greater.next = None
        
        # connect both lists
        less.next = greater_dummy.next
        
        return less_dummy.next