
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def _get_leaves(node):
            
            leaves = []
            if not node:
                return leaves
            
            stack = [node]
            while stack:
                current_node = stack.pop()
                
                
                if not current_node.left and not current_node.right:
                    leaves.append(current_node.val)
                
               
                if current_node.right:
                    stack.append(current_node.right)
                if current_node.left:
                    stack.append(current_node.left)
            return leaves
        
        
        first_leaves = _get_leaves(root1)
        second_leaves = _get_leaves(root2)
        
       
        return first_leaves == second_leaves