class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()  # Step 1: sort

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # Try pairing lightest + heaviest
            if people[left] + people[right] <= limit:
                left += 1  # light person used
            
            # heavy person always goes
            right -= 1
            boats += 1  # one boat used

        return boats