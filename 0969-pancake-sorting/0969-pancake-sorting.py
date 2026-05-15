class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        ans = []

        n = len(arr)

        # place biggest elements from right -> left
        for last in range(n - 1, -1, -1):

            # find index of largest element from 0 -> last
            max_index = 0

            for i in range(last + 1):

                if arr[i] > arr[max_index]:
                    max_index = i

            # already in correct position
            if max_index == last:
                continue

            # bring largest element to front
            if max_index != 0:

                arr[:max_index + 1] = reversed(arr[:max_index + 1])

                ans.append(max_index + 1)

            # move largest element to correct position
            arr[:last + 1] = reversed(arr[:last + 1])

            ans.append(last + 1)

        return ans