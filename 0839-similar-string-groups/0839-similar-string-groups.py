class Solution:
    def numSimilarGroups(self, strs):
        # number of strings
        n = len(strs)

        # visited array to track which strings are already grouped
        visited = [False] * n

        # function to check if two strings are similar
        def is_similar(s1, s2):
            # count how many positions are different
            diff = 0

            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1

                # if more than 2 differences → cannot fix with one swap
                if diff > 2:
                    return False

            # valid only if 0 or 2 mismatches
            return diff == 0 or diff == 2

        # DFS function to explore all connected strings
        def dfs(i):
            # mark current string as visited
            visited[i] = True

            # try to connect with every other string
            for j in range(n):
                # if not visited and similar → explore further
                if not visited[j] and is_similar(strs[i], strs[j]):
                    dfs(j)

        # count number of groups
        groups = 0

        # go through every string
        for i in range(n):

            # if this string is not yet visited → new group
            if not visited[i]:
                groups += 1

                # explore all strings connected to this one
                dfs(i)

        return groups