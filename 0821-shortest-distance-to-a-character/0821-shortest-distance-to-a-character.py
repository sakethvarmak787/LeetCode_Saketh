class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        hashmap = {}
        hashmap[c]= [] 
        for i in range(len(s)):
            if s[i] == c:
                hashmap[c].append(i)

        ans = []
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
                continue
            min_len = float('inf')
            for idx in hashmap[c]:
                min_len = min(min_len,abs(idx-i))

            ans.append(min_len)

        return ans