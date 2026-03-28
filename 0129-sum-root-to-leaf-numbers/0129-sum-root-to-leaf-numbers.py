class Solution:
    def sumNumbers(self, root):
        
        def dfs(node, curr_num):
            if not node:
                return 0
            
            curr_num = curr_num * 10 + node.val
            
            # if leaf → return the number
            if not node.left and not node.right:
                return curr_num
            
            return dfs(node.left, curr_num) + dfs(node.right, curr_num)
        
        return dfs(root, 0)