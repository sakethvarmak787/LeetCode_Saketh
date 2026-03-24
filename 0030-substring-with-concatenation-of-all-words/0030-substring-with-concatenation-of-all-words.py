class Solution:
    def findSubstring(self, s, words):
        
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        
        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1
        
        res = []
        
        # try all offsets (VERY IMPORTANT)
        for i in range(word_len):
            
            left = i
            right = i
            
            seen = {}
            count = 0  # number of valid words in window
            
            while right + word_len <= len(s):
                
                # take word from right
                word = s[right:right + word_len]
                right += word_len
                
                # case 1: word is valid
                if word in word_count:
                    
                    seen[word] = seen.get(word, 0) + 1
                    count += 1
                    
                    # too many of same word → shrink
                    while seen[word] > word_count[word]:
                        
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    # valid window found---> here we get the index of that word
                    if count == total_words:
                        res.append(left)
                
                # case 2: invalid word → reset
                else:
                    seen.clear()
                    count = 0
                    left = right
        
        return res