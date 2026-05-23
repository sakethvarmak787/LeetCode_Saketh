class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # locations go till 1000
        arr = [0] * 1001

        # mark start and stop
        for passengers, start, end in trips:

            # passengers enter
            arr[start] += passengers

            # passengers leave
            arr[end] -= passengers

        current = 0

        # prefix sum
        for i in range(1001):

            current += arr[i]

            # exceeded capacity
            if current > capacity:

                return False

        return True