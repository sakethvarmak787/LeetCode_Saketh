class Solution:
    def dailyTemperatures(self, temperatures):
        # Step 1: Prepare result array with default 0
        n = len(temperatures)
        answer = [0] * n

        # This stack will store indices of days
        # These are days that are still "waiting" for a warmer temperature
        stack = []

        # We go day by day from left to right
        for i in range(n):

            # While stack is not empty AND
            # current temperature is greater than the temperature
            # of the day at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Pop the previous day index
                prev_day = stack.pop()

                # Now we have found a warmer day for prev_day
                # So we calculate how many days it took
                answer[prev_day] = i - prev_day

                # WHY:
                # We are resolving that day now,
                # so we don't need to check it again in the future

            # After resolving all possible days,
            # we push current day into stack
            # because it is now waiting for its warmer day
            stack.append(i)

        return answer