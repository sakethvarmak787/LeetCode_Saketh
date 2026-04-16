from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        
        # Step 1: count frequency of each task
        freq = Counter(tasks)
        
        # Step 2: find the maximum frequency
        # This tells us which task appears the most
        max_freq = max(freq.values())
        
        # Step 3: count how many tasks have this max frequency
        # Why? Because multiple tasks can compete for the same last slots
        count_max = 0
        for task in freq:
            if freq[task] == max_freq:
                count_max += 1
        
        # Step 4: calculate the frame size
        # (max_freq - 1) because last occurrence doesn't need a gap after it
        # (n + 1) because each block includes the task itself + cooldown slots
        frames = (max_freq - 1) * (n + 1)
        
        # Step 5: add the last occurrences of the most frequent tasks
        # Example: A and B both have max frequency → both fill last positions
        result = frames + count_max
        
        # Step 6: compare with total tasks
        # If enough tasks exist, no idle needed
        return max(len(tasks), result)