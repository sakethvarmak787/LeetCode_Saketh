class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.temp = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.temp.append(node) 
            dfs(node.right)
        
        dfs(root)
        srt = sorted(node.val for node in self.temp)
        for i in range(len(srt)):
            self.temp[i].val = srt[i]