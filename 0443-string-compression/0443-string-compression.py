class Solution:
    def compress(self, chars: list[str]) -> int:
        # 1. Create a temporary list (the brute force "scratchpad")
        res = []
        
        i = 0
        while i < len(chars):
            current_char = chars[i]
            count = 0
            
            # Count how many times this character repeats
            while i < len(chars) and chars[i] == current_char:
                count += 1
                i += 1
            
            # Add the character to our scratchpad
            res.append(current_char)
            
            # If it appeared more than once, add the count as characters
            if count > 1:
                for digit in str(count):
                    res.append(digit)
        
        # 2. Modify 'chars' in-place so the judge can see the result
        # This is where we copy everything from 'res' back into 'chars'
        for j in range(len(res)):
            chars[j] = res[j]
            
        # 3. Return the length of the compressed part
        return len(res)