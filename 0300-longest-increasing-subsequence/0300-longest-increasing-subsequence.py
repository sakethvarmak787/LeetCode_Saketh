class Solution:
    def lengthOfLIS(self, nums):
        lst = [nums[0]]   # smallest tail of length 1
        max_len = 1       # length of LIS so far

        for num in nums[1:]:

            # CASE 1: can extend sequence
            if num > lst[-1]:
                lst.append(num)
                max_len += 1

            # CASE 2: replace to keep better future options
            else:
                ind = 0

                # find first element >= num
                while ind < len(lst) and lst[ind] < num:
                    ind += 1

                lst[ind] = num   # replace

        return max_len