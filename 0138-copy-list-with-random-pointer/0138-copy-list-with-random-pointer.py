class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: insert copied nodes
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        # Step 2: assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: separate the lists
        curr = head
        copy_head = head.next
        copy = copy_head

        while curr:
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next

            curr = curr.next
            copy = copy.next

        return copy_head