class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        # This will store the best answer found so far
        best_word = ""
        
        # Go through each word in the dictionary
        for word in dictionary:
            
            # -----------------------------
            # STEP 1: Check if "word" is a subsequence of "s"
            # -----------------------------
            
            i = 0  # pointer for s
            j = 0  # pointer for word
            
            # Traverse through string s
            while i < len(s) and j < len(word):
                
                # If characters match, we move j forward
                # WHY? Because we successfully matched one character of word
                if s[i] == word[j]:
                    j += 1
                
                # Always move i forward
                # WHY? Because we are scanning s completely
                i += 1
            
            # After loop:
            # If j reached end → we matched entire word
            if j == len(word):
                
                # -----------------------------
                # STEP 2: Update best answer
                # -----------------------------
                
                # Case 1: current word is longer
                if len(word) > len(best_word):
                    best_word = word
                
                # Case 2: same length → choose lexicographically smaller
                elif len(word) == len(best_word) and word < best_word:
                    best_word = word
        
        return best_word