from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        bank_set = set(bank)
        
        # if endGene not in bank → cannot reach
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])  # (current_gene, steps)
        visited = set([startGene])
        
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            curr, steps = queue.popleft()
            
            # if reached target
            if curr == endGene:
                return steps
            
            # try all possible mutations
            for i in range(8):
                for ch in genes:
                    
                    if curr[i] == ch:
                        continue
                    
                    new_gene = curr[:i] + ch + curr[i+1:]
                    
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
        
        return -1