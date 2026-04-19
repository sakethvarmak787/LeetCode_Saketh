class Solution:
    def grayCode(self, n: int):
        # Start with base case
        # For n = 0 → only one number: 0
        result = [0]

        # We build the sequence step by step for each bit
        for i in range(n):
           
            add_bit = 1 << i
            
            # Traverse reversed list
            for num in reversed(result):
                # Turn ON the i-th bit using OR
                
                # WHY OR?
                # Because we want to add this new bit without affecting others
                
                new_num = num | add_bit
                
                # Append to result
                result.append(new_num)

        return result