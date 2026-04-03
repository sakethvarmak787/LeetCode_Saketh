class Solution:
    def wordBreak(self, s: str, wordDict):
        
        wordSet = set(wordDict)  # fast lookup
        
        dp = [False] * (len(s) + 1)
        dp[0] = True   # empty string is valid
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                
                # if left part is valid AND right part is a word
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[len(s)] #if last is true we found all