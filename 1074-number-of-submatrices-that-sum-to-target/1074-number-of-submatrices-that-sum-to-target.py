from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        count = 0

        for left in range(cols):

            row_sum = [0] * rows

            for right in range(left, cols):

                for r in range(rows):
                    row_sum[r] += matrix[r][right]

                prefix = 0
                freq = defaultdict(int)
                freq[0] = 1

                for num in row_sum:

                    prefix += num

                    count += freq[prefix - target]

                    freq[prefix] += 1

        return count