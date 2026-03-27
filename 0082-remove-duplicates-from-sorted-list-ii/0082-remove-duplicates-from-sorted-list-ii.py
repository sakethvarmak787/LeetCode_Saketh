class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            # check if current node is duplicate
            if curr.next and curr.val == curr.next.val:
                
                # skip all nodes with same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                # remove all duplicates
                prev.next = curr.next
            
            else:
                # move prev only if no duplicate
                prev = prev.next
            
            # always move curr
            curr = curr.next
        
        return dummy.next