class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        greatest_so_far = -1

        for i in range(len(arr) - 1, -1, -1):

            temp = arr[i]

            arr[i] = greatest_so_far

            greatest_so_far = max(greatest_so_far, temp)

        return arr