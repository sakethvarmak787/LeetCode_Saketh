class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()
        
        for num in arr:
            curr = {num}
            for x in prev:
                curr.add(num | x)
            res.update(curr)
            prev = curr
        
        return len(res)