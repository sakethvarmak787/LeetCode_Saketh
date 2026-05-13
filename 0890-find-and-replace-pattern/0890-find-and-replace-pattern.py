class Solution:
    def findAndReplacePattern(self, words, pattern):

        def isIsomorphic(s, t):

            mapST = {}
            mapTS = {}

            for i in range(len(s)):

                c1 = s[i]
                c2 = t[i]

                # s -> t
                if c1 in mapST:
                    if mapST[c1] != c2:
                        return False
                else:
                    mapST[c1] = c2

                # t -> s
                if c2 in mapTS:
                    if mapTS[c2] != c1:
                        return False
                else:
                    mapTS[c2] = c1

            return True

        ans = []

        for word in words:
            if isIsomorphic(pattern, word):
                ans.append(word)

        return ans