class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        # difference array
        answer = [0] * n

        # mark ranges
        for first, last, seats in bookings:

            # start adding seats
            answer[first - 1] += seats

            # stop adding after last
            if last < n:
                answer[last] -= seats

        # prefix sum
        for i in range(1, n):

            answer[i] += answer[i - 1]

        return answer