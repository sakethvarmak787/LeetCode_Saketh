class Solution:
    def maxPathSum(self, root):
        self.maxPathSum = float("-inf")

        def pathSum(root):
            if not root:
                return 0

            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))

            self.maxPathSum = max(self.maxPathSum,left + right + root.val)

            return max(left, right) + root.val

        pathSum(root)
        return self.maxPathSum