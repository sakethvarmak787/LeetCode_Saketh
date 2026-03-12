class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        freq = {}

        def dfs(node):
            if not node:
                return
            
            freq[node.val] = freq.get(node.val, 0) + 1
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(freq.values())

        res = []
        for k,v in freq.items():
            if v == max_freq:
                res.append(k)

        return res