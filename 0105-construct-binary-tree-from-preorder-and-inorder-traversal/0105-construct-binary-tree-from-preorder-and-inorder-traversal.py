from collections import deque

# Definition for a binary tree node.
#class TreeNode:
 #   def __init__(self, val=0, left=None, right=None):
 #       self.val = val
  #      self.left = left
  #      self.right = right


class Solution:
    def buildTree(self, preorder, inorder):

        # convert preorder to queue
        p = deque(preorder)

        # total nodes
        N = len(preorder)

        # hashmap for inorder indices
        lookup = {v: i for i, v in enumerate(inorder)}

        def rec(start, end):
            # base case
            if start > end:
                return None

            # get root from preorder
            cand = p.popleft()
            root = TreeNode(cand)

            # find position in inorder
            middle = lookup[cand]

            # build left subtree
            root.left = rec(start, middle - 1)

            # build right subtree
            root.right = rec(middle + 1, end)

            return root

        return rec(0, N - 1)