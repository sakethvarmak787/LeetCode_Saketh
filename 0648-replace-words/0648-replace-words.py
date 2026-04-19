class Solution:
    def replaceWords(self, dictionary, sentence):
        
        # Step 1: Split the sentence into words
        # WHY: We want to process each word independently
        words = sentence.split()
        
        # This will store the final transformed words
        result = []
        
        # Step 2: Process each word one by one
        for word in words:
            
            # This variable will store the best (shortest) root found so far
            # Initially, we assume no root matches
            shortest_root = None
            
            # Step 3: Try every root in dictionary
            # WHY: brute force means we try all possibilities
            for root in dictionary:
                
                # Check if current root is a prefix of the word
                # WHY: problem defines derivative as prefix match
                if word.startswith(root):
                    
                    # If this is the first match OR we found a shorter root
                    # WHY: we must pick the shortest root among all matches
                    if shortest_root is None or len(root) < len(shortest_root):
                        shortest_root = root
            
            # Step 4: After checking all roots
            if shortest_root is not None:
                # If we found a matching root → replace the word
                result.append(shortest_root)
            else:
                # If no root matched → keep original word
                result.append(word)
        
        
        # Step 5: Join all processed words back into a sentence
        return " ".join(result)


