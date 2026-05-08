class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case for n = 1
        if n == 1:
            return "1"
        
        # Start with the sequence for n = 1
        current_str = "1"
        
        # Generate the sequence up to n
        for _ in range(n - 1):
            next_str = ""
            i = 0
            
            # Use Run-Length Encoding (RLE) logic
            while i < len(current_str):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_str) and current_str[i] == current_str[i+1]:
                    count += 1
                    i += 1
                
                # Append the "count" followed by the "digit"
                next_str += str(count) + current_str[i]
                i += 1
            
            current_str = next_str
            
        return current_str