class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums) - 1

                while l<r:
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr_sum == target:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1

                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1

        return list(set(res))
            


    

