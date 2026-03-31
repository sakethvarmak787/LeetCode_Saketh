class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        # helper to merge two lists
        def merge(l1, l2):
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
            
            tail.next = l1 if l1 else l2
            return dummy.next
        
        # divide and conquer
        def divide(lists):
            if len(lists) == 1:
                return lists[0]
            
            mid = len(lists) // 2
            
            left = divide(lists[:mid])
            right = divide(lists[mid:])
            
            return merge(left, right)
        
        return divide(lists)