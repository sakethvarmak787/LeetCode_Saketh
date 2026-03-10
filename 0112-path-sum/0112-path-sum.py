class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False 
        
        def dfs(node, current_sum):
            if not node:
                return
            
           
            current_sum += node.val
            
          
            if not node.left and not node.right:
                if current_sum == targetSum:
                    self.found = True
                return

         
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            

        dfs(root, 0)
        return self.found