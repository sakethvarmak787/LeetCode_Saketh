class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        res = [None] * total_len
        
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return ""  
                    res[i + j] = str2[j]
        
        for i in range(total_len):
            if res[i] is None:
                res[i] = 'a'
        
        for i in range(n):
            if str1[i] == 'F':
                is_match = True
                for j in range(m):
                    if res[i + j] != str2[j]:
                        is_match = False
                        break
                if is_match:
                    changed = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        fixed_by_t = False
                    
                        for p in range(max(0, idx - m + 1), min(n, idx + 1)):
                            if str1[p] == 'T':
                                fixed_by_t = True
                                break
                        
                        if not fixed_by_t:
                            res[idx] = 'b'
                            changed = True
                            break
                    
                    if not changed:
                        return "" 
                        
        return "".join(res)