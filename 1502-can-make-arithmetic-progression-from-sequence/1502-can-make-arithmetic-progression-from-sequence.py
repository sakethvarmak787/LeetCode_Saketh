class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr,reverse = True)
        res = []
        for i in range(1,len(arr)):
            res.append(abs(arr[i]-arr[i-1]))
        return len(set(res)) == 1
