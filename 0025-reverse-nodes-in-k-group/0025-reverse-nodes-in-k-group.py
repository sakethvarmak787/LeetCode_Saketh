class Solution:
    def reverseKGroup(self, head, k):
        
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        
        group_prev = dummy
        
        while True:
            # find kth node
            kth = getKth(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next
            
            # reverse group
            prev = group_next
            curr = group_prev.next
            
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # reconnect
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next