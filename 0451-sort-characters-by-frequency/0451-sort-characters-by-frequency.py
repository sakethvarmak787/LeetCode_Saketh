from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        dictt = Counter(s)

        ans = []

        for ch in dictt:
            ans.append((dictt[ch], ch))

        ans.sort(key=lambda x: x[0], reverse=True)

        res = []

        for i in range(len(ans)):
            freq = ans[i][0]
            ch = ans[i][1]

            res.append(ch * freq)

        final = ''.join(res)

        return final