class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)

        # Step 1: Find longest non-decreasing prefix
        left_end = 0
        while left_end < n - 1 and arr[left_end] <= arr[left_end + 1]:
            left_end += 1

        # If entire array is sorted, no need to remove anything
        if left_end == n - 1:
            return 0

        # Step 2: Find longest non-decreasing suffix
        right_start = n - 1
        while right_start > 0 and arr[right_start - 1] <= arr[right_start]:
            right_start -= 1

        # Step 3: Initial answer (remove one side completely)
        # Either remove suffix after prefix OR prefix before suffix
        min_len = min(n - left_end - 1, right_start)

        # Step 4: Try merging prefix and suffix using two pointers
        i = 0
        j = right_start

        while i <= left_end and j < n:

            if arr[i] <= arr[j]:
                # Valid connection → we can merge prefix till i
                # and suffix from j onwards
                # Removed subarray is between them
                min_len = min(min_len, j - i - 1)
                i += 1
            else:
                # Not valid → we need a bigger value on right side
                # So move j forward
                j += 1

        return min_len