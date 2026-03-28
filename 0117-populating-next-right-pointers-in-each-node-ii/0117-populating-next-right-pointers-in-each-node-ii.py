from collections import deque

#class Node:
 #   def __init__(self, val=0, left=None, right=None, next=None):
   #     self.val = val
    #    self.left = left
    #    self.right = right
    #    self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            prev.next = None

        return root