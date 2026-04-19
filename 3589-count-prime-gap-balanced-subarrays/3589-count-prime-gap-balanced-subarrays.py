from collections import deque
from typing import List

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        def is_prime(n):
            if n < 2: return False
            if n < 4: return True
            if n % 2 == 0 or n % 3 == 0: return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0: return False
                i += 6
            return True

        n = len(nums)
        prime_idx = [i for i in range(n) if is_prime(nums[i])]
        m = len(prime_idx)

        if m < 2:
            return 0

        # left_choices[i] = how many left endpoints "own" prime i
        left_choices = [prime_idx[i] - (prime_idx[i-1] if i > 0 else -1) for i in range(m)]

        # prefix[i] = sum of left_choices[0..i-1]
        prefix = [0] * (m + 1)
        for i in range(m):
            prefix[i + 1] = prefix[i] + left_choices[i]

        max_dq, min_dq = deque(), deque()
        ans = 0
        l = 0

        for r in range(m):
            while max_dq and nums[prime_idx[max_dq[-1]]] <= nums[prime_idx[r]]:
                max_dq.pop()
            max_dq.append(r)

            while min_dq and nums[prime_idx[min_dq[-1]]] >= nums[prime_idx[r]]:
                min_dq.pop()
            min_dq.append(r)

            while nums[prime_idx[max_dq[0]]] - nums[prime_idx[min_dq[0]]] > k:
                l += 1
                if max_dq[0] < l: max_dq.popleft()
                if min_dq[0] < l: min_dq.popleft()

            if r >= l + 1:
                right_choices = ((prime_idx[r+1] - 1) if r + 1 < m else n - 1) - prime_idx[r] + 1
                # Sum left_choices[l..r-1] in O(1) using prefix sums
                ans += (prefix[r] - prefix[l]) * right_choices

        return ans