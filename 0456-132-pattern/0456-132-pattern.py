class Solution:
    def find132pattern(self, nums):
        # This will store potential "3" values (nums[j])
        stack = []

        # This will store the best candidate for "2" (nums[k])
        third = float('-inf')

        # Traverse from right to left
        for num in reversed(nums):

            # If current number is less than "third",
            # it means we found nums[i] < nums[k]
            # And since "third" came from stack,
            # it already satisfies nums[k] < nums[j]
            if num < third:
                # ===============================
                # DRY RUN:
                # nums = [3,1,4,2]
                # At num = 1:
                # third = 2
                # 1 < 2 → pattern found
                # ===============================
                return True

            # While current number is greater than stack top,
            # we pop from stack and update "third"
            # This means we found a better candidate for nums[k]
            while stack and num > stack[-1]:

                popped = stack.pop()

                # Update third to the last popped value
                # This becomes our best "middle" value
                third = popped

                # ===============================
                # DRY RUN:
                # num = 4
                # stack = [2]
                # pop 2 → third = 2
                # ===============================

            # Push current number into stack
            # It can act as future nums[j]
            stack.append(num)

            # ===============================
            # DRY RUN:
            # num = 2 → stack = [2]
            # num = 4 → stack = [4]
            # ===============================

        # If no pattern found
        return False