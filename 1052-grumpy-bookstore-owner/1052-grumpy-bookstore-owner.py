class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # already satisfied customers
        base = 0

        for i in range(len(customers)):

            if grumpy[i] == 0:
                base += customers[i]

        ans = base
        for j in range(len(customers) - minutes + 1):

            extra = 0
            for k in range(j, j + minutes):

                if grumpy[k] == 1:
                    extra += customers[k]

            ans = max(ans, base + extra)

        return ans