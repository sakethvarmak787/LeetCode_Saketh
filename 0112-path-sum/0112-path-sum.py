class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # if leaf node check for the condition as we came to last
        if not root.left and not root.right:
            return targetSum == root.val
        
        # check left or right subtree
        remaining = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))