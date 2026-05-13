class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = Counter(secret)
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull+=1
                freq[secret[i]]-=1

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if freq.get(guess[i], 0) > 0: #if the frequency of char is greater than 0
                    cow += 1
                    freq[guess[i]] -= 1
                    
        return "{}A{}B".format(bull,cow)
        
