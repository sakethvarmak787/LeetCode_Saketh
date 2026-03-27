from collections import deque

# Definition for a binary tree node.
#class TreeNode:
    #def __init__(self, val=0, left=None, right=None):
    #    self.val = val
    #    self.left = left
    #    self.right = right


class Solution:
    def buildTree(self, inorder, postorder):

        # convert postorder into deque (we will pop from end)
        p = deque(postorder)

        # map value -> index in inorder
        lookup = {v: i for i, v in enumerate(inorder)}

        def rec(start, end):
            # base case
            if start > end:
                return None

            # take root from end of postorder
            val = p.pop()
            root = TreeNode(val)

            # find root position in inorder
            mid = lookup[val]

            # IMPORTANT: build right first
            root.right = rec(mid + 1, end)

            # then build left
            root.left = rec(start, mid - 1)

            return root

        return rec(0, len(inorder) - 1)