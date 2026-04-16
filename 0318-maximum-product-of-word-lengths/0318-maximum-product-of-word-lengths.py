class Solution:
    def maxProduct(self, words):
        # Initialize the result to 0
        # This will store the maximum product we find
        max_product = 0
        
        # Outer loop → pick the first word
        for i in range(len(words)):
            # Inner loop → pick the second word
            # We start from i+1 so we don't repeat pairs
            for j in range(i + 1, len(words)):
                
                # Convert both words into sets of characters
                # WHY? → So we can easily check if they share letters
                set1 = set(words[i])
                set2 = set(words[j])
                
                # Check if they have any common characters
                # If intersection is empty → valid pair
                if len(set1.intersection(set2)) == 0:
                    
                    # Calculate product of lengths
                    product = len(words[i]) * len(words[j])
                    
                    # Update max if needed
                    max_product = max(max_product, product)
                    
                    # ---------------- PARALLEL DRY RUN ----------------
                    # Example:
                    # words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
                    #
                    # i = 0 ("abcw"), j = 2 ("foo")
                    # set1 = {a,b,c,w}, set2 = {f,o}
                    # intersection = empty → valid
                    # product = 4 * 3 = 12 → max = 12
                    #
                    # i = 0 ("abcw"), j = 4 ("xtfn")
                    # set1 = {a,b,c,w}, set2 = {x,t,f,n}
                    # intersection = empty → valid
                    # product = 4 * 4 = 16 → max = 16
                    # --------------------------------------------------
        
        # Return the final maximum product
        return max_product