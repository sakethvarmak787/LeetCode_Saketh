from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        dictt = Counter(words[0])
        res = []

        for i in range(1, len(words)):
            
            temp = []
            
            for ch in words[i]:
                
                if ch in dictt and dictt[ch] != 0:
                    temp.append(ch)
                    dictt[ch] -= 1
            
            dictt = Counter(temp)

        return list(dictt.elements())