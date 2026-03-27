class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length and tail
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        # Step 2: make it circular
        tail.next = head
        
        # Step 3: reduce k
        k = k % length
        
        # Step 4: find new tail (length - k - 1 steps)
        steps = length - k
        new_tail = head
        
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        # Step 5: break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head