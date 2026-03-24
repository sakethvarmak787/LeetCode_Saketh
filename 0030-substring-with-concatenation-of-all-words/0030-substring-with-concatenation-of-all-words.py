class Solution:
    def findSubstring(self, s, words):
        
        # result list to store valid starting indices
        res = []
        
        # length of each word
        word_len = len(words[0])
        
        # total number of words
        total_words = len(words)
        
        # total length of concatenated substring
        total_len = word_len * total_words
        
        # build frequency map of given words
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # go through every possible starting index
        for i in range(len(s) - total_len + 1):
            
            # dictionary to track words we see in current window
            seen = {}
            
            # we will try to match all words
            j = 0
            
            # try to take words one by one from substring
            while j < total_words:
                
                # calculate start index of current word
                start = i + j * word_len
                
                # extract word of size word_len
                word = s[start:start + word_len]
                
                # if word is not in expected list, break early
                if word not in word_count:
                    break
                
                # add to seen count
                seen[word] = seen.get(word, 0) + 1
                
                # if frequency exceeds expected → invalid
                if seen[word] > word_count[word]:
                    break
                
                # move to next word
                j += 1
            
            # if we matched all words → valid index
            if j == total_words:
                res.append(i)
        
        return res