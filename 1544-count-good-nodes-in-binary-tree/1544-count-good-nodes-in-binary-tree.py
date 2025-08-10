class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root, check):
            if root.val >= check:
                self.good += 1
            
            if root.left:
                dfs(root.left, max(check, root.val))
            
            if root.right:
                dfs(root.right, max(check, root.val))

        dfs(root, root.val)
        return self.good